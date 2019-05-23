import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS 


#执行api调用并存储响应

url="https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("Status code: ",r.status_code)

#将api响应存储在一个变量中
response_dict=r.json()
print("总数，total_count: ",response_dict['total_count'])

# 研究有关仓库信息
repo_dicts=response_dict['items']

names,stars=[],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# print("name:",names)
# 可视化

my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_labe=15
my_config.show_y_guides=False
my_config.width=1000



chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title="most-starred python projects on github"
chart.x_labels=names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
print("查看图表")



# print("repositories returned: ",len(repo_dicts))

# repo_dict=repo_dicts[0]

# print("\nSelected information about first repository:")

# for repo_dict in repo_dicts:
#     print("name:",repo_dict['name'])
#     print("owner",repo_dict['owner']['login'])
#     print("stars:",repo_dict['stargazers_count'])
#     print("repository",repo_dict["html_url"])
#     print("created",repo_dict["created_at"])
#     print("updated",repo_dict["updated_at"])
#     print("描述",repo_dict["description"])

# print("\nKeys:",len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)

#输入结果
# print(response_dict.keys())



