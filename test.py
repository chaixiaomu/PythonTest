import requests

#url = "https://www.zhihu.com/api/v4/columns/reinhardtjin/followers"
url1 = "https://www.zhihu.com/api/v4/columns/pythoneer/followers"
url2="https://xiaoce-timeline-api-ms.juejin.im/v1/getListByLastTime"

params1={"uid":"5ce35c27e51d45109b01b101",
         "client_id":"1558404127605",
        #  "token":"eyJhY2Nlc3NfdG9rZW4iOiJsYnBzWVp1SkVDeTJHdFUzIiwicmVmcmVzaF90b2tlbiI6IktiOVE4SmgwbUdNd3E1a3IiLCJ0b2tlbl90eXBlIjoibWFjIiwiZXhwaXJlX2luIjoyNTkyMDAwfQ==",
         "src":"web",
         "pageNum":1
        }

headers1={
    "Origin":"https://juejin.im",
    "Referer":"https://juejin.im/books",
    # "User-Agent","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (HTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

params={"limit":40,
        "offset":40,
        "include":"data[*].follower_count,gender,is_followed,is_following"}

headers={
    "authority": "www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (HTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

r = requests.get(url2,headers=headers1,params=params1)
print("请求url地址：",r.url)
print("返回数据：",r.text)


follower = r.json()
print("正常编码：",follower)



