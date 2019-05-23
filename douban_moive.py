import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#请求的url
url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
url1='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

#进行请求并返回响应结果
r=requests.get(url)
print("请求结果：",r.status_code)

#将请求结果词典化后存储起来
response_dict=r.json()
print("键值对：",response_dict.keys())

response_dicts=response_dict['data']
print("返回的数据：",len(response_dicts))
print("response_dicts[0]:",response_dicts[0])

response_dict=response_dicts[0]
print("\nKeys:",len(response_dict))
for key in sorted(response_dict.keys()):
    print(key)

#输出第一部电影的数据
# print(" \n select information about first movie:")
# print("title:",response_dict['title'])
# print("casts:",response_dict['casts'])
# print("directors:",response_dict['directors'])
# print("id:",response_dict['id'])
# print("star:",response_dict['star'])
# print("rate:",response_dict['rate'])
# print("url:",response_dict['url'])

titles,rates=[],[]
#输入响应的所有电影信息
print(" \n select information about each movie:")
for response_dict in response_dicts:
    titles.append(response_dict['title'])
    rates.append(float(response_dict['rate']))
    # print("title:",response_dict['title'])
    # print("casts:",response_dict['casts'])
    # print("directors:",response_dict['directors'])
    # print("id:",response_dict['id'])
    # print("star:",response_dict['star'])
    # print("rate:",response_dict['rate'])
    # print("url:",response_dict['url'])

print("电影名字：",titles)
print("电影评分",rates)

#可视化处理电影及评分
my_style = LS('#333366',base_style=LCS)
chart =pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title="豆瓣电影-最新上映评分"
chart.x_labels=titles
chart.add('',rates)
chart.render_to_file('douban.svg')
print("图片已生成")

#把抓取到的数据存储到.txt 文件中

filename='douban.txt'
with open(filename,'w') as file_object:
    file_object.write(str(response_dicts))
    # file_object.write('World is powered by solitude.\n')
print('运行成功')