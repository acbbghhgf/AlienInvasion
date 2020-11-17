import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# 将 API 响应存储在一个变量中
resquests_dict = r.json()
#print("Total repositories:", resquests_dict['total_count'])

#探究有关仓库的信息
repo_dicts = resquests_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    names.append(repo_dict['name'])
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'xlink' : repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
    
# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
#chart = pygal.Bar(style = my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Start Python Projects on GitHub"
chart.x_labels = names


chart.add('', plot_dicts)
chart.render_to_file('plot-python_repos.svg')
