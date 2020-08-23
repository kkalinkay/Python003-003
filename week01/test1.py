import requests
from bs4 import BeautifulSoup
import lxml.etree
import pandas as pd
from time import sleep

#作业说明
#安装并使用 requests、bs4 库
# 爬取猫眼电影（最受期待榜）的前 10 个电影名称、电影类型和上映时间
# 并以 UTF-8 字符集保存到 csv 格式的文件中。

myurl='https://maoyan.com/board/6'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

resp=requests.get(url=myurl,headers=header)

#将返回写入文件
# with open('maoyan.txt','a+',encoding='utf-8') as f:
#     f.write(resp.text)

bs_info=BeautifulSoup(resp.text,'html.parser')

#取得前10个电影的链接
urls=[]
for movie in bs_info.find_all('p',attrs={'class':'name'}):
    link = movie.find('a').get('href')
    #title = movie.find('a').get('title')
    #time = movie.find_all('p',attrs={'class':'releasetime'}).text()
    urls.append(f'https://maoyan.com{link}')
    #print(title)

print(urls)


#get电影详情链接，取得电影类型和上映时间数据
def getmovieurl(movieurl):
    response=requests.get(url=movieurl,headers=header)
    xpath_info = lxml.etree.HTML(response.text)
    #电影名称
    title = xpath_info.xpath('//div[@class="movie-brief-container"]/h1/text()')
    #print(title)
    #电影类型
    type=xpath_info.xpath('//li[@class="ellipsis"]/a/text()')
    #print(type)
    #上映时间
    movie_date=xpath_info.xpath('//li[@class="ellipsis"][last()]/text()')
    #print(movie_date)
    # movie_info = {"电影名称": title, "影片类型": '/'.join(type), "上映日期": movie_date}

    movie_info = [title[0], '/'.join(type), movie_date[0]]
    print(movie_info)
    return movie_info


#date = pd.DataFrame(data=movie_info)
movie_data = {"电影名称": [], "影片类型": [], "上映日期": []}
for movieurl in urls:
    data = getmovieurl(movieurl)
    sleep(5)
    movie_data.get("电影名称").append(data[0])
    movie_data.get("影片类型").append(data[1])
    movie_data.get("上映日期").append(data[2])

movie_data = pd.DataFrame(movie_data)
movie_data.to_csv('./test1_movie.csv', encoding='utf-8', index=False)
