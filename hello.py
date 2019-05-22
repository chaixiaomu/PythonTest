# -*- coding: utf-8 -*-
__author__ = "liuzhijun"

import requests


def crawl():
    # url中的参数需要根据自己的情况做调整
    url="https://mp.weixin.qq.com/mp/profile_ext?" \
        "action=home&" \
        "__biz=MzI2NDk5NzA0Mw==&scene=126" \
        "&bizpsid=1558515777&" \
        "sessionid=1558515777&" \
        "sharer_username=gh_240fbf8b33e4&" \
        "subscene=0&" \
        "clicktime=1558516372&" \
        "devicetype=iOS12.3&" \
        "version=1700042b&" \
        "lang=zh_CN&" \
        "nettype=WIFI&" \
        "a8scene=0&" \
        "fontScale=100&" \
        "pass_ticket=dwyLHQT1MfPawnvZ%2BRvpEF294w8gJmpPMELUAKwSfmjale8iu%2FbEzB2%2FrHbZez%2Bo&wx_header=1" \



    
    url1 = "https://mp.weixin.qq.com/mp/profile_ext?" \
          "action=home&" \
          "__biz=MjM5MzgyODQxMQ==&" \
          "scene=124&" \
          "devicetype=iOS10.3.3&" \
          "version=16060022&" \
          "lang=zh_CN&nettype=WIFI&a8scene=3&" \
          "fontScale=100&" \
          "pass_ticket=CSprpmr8jgRyCI4Y%2FW9Er99kmPVPzaKYXOTD140oDqj%2Bs%2F69p7m09jaVxogugn%2BX&" \
          "wx_header=1"

    headers = """
Host :mp.weixin.qq.com
Cookie: devicetype=iOS10.3.3; lang=zh_CN; pass_ticket=CSprpmr8jgRyCI4Y/W9Er99kmPVPzaKYXOTD140oDqj+s/69p7m09jaVxogugn+X; version=16060022; wap_sid2=CIDUopEDEogBZ3N6WEpELUg0aHNna00zTEdMbF9fT1V5UEZYempsNVlzUU1SUGlLZnFOeEhqbDBjN1J0My1Wem1hcmk5WW9oUkR3eUl0UGkzUW93YXFXUlRUcU9pR2FyZEVwZUtYeDNfek1lbmdqRFFHT29hNHc4akM4Y1VyWTB0M2w4UnYybzBxQU1BQUF+fjCD+u3RBTgNQJVO; wxuin=841525760; rewardsn=69a79c8f8c8cca51cda1; wxtokenkey=e1ae7dc0f4af23cea1ab64d0b5d22bcc2d1ffe433448e5392fd9b7aaa0b214f4; ua_id=seRYVLVNcjYoZPzpAAAAACA8ySAXhkrd89FL3uvLbt8=; _scan_has_moon=1; pgv_info=ssid=s1123443900; pt2gguin=o0253421576; ptcz=3d9558280f480d9453cc13b78b32059793c778a1e8aa723ce7b2f5e9744f606b; pgv_pvid=7330882815; pgv_pvi=8857346048; sd_cookie_crttime=1510571099034; sd_userid=34241510571099034; pvid=6161617834; RK=7JMfU7Y+Gq
X-WECHAT-KEY: ccb9edae454e7febaec09e5c7d64e04704ddd83bb21867f97ddde102232f86f6cc48db3d258a6c54ddac908d096703ac21c7622245dce01f2c441d299292088b72001090580b35636edd27a9403273be
X-WECHAT-UIN: Mjc3MzAzMjMwNQ%3D%3D
Accept :text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent :Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN
Accept-Language :zh-cn
Accept-Encoding :br, gzip, deflate
Connection :keep-alive



    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    if '<title>验证</title>' in response.text:
        raise Exception("获取微信公众号文章失败，可能是因为你的请求参数有误，请重新获取")
    data = extract_data(response.text)
    for item in data:
        print(item)


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles


def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


if __name__ == '__main__':
    crawl()
