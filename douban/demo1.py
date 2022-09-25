# -*- coding: utf-8 -*-
import time

from lxml import etree
import pandas as pd
import requests


def insertElement(list, temp):
    for item in temp:
        list.append(item)


# 豆瓣电影top250
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

# 电影排名
movieRanking = []
# 电影名称(中文)
movieName = []
# 电影评分
rating = []
# 电影标语
quote = []
# url开始位置
for start in range(0, 250, 25):
    BASE_URL = "https://movie.douban.com/top250?start=" + str(start) + "&filter="
    try:
        htmlTest = requests.get(url=BASE_URL, headers=headers).text
        analysisHtml = etree.HTML(htmlTest)
        movieList = analysisHtml.xpath('//*[@id="content"]/div/div[1]/ol/li/div[1]')
        # 当前电影排名
        movieRankingTemp = movieList[0].xpath('//div/em/text()')
        insertElement(movieRanking, movieRankingTemp)
        # 当前电影名称(中文)
        movieNameTemp = movieList[0].xpath('//div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
        insertElement(movieName, movieNameTemp)
        # 该电影评分
        ratingTemp = movieList[0].xpath('//div[@class="bd"]/div[@class="star"]/span[2]/text()')
        insertElement(rating, ratingTemp)
    except Exception as e:
        print(e)
    print("第" + str(start) + "查询完成")
    time.sleep(2)

data = {
    "电影排名": pd.Series(movieRanking),
    "电影名称": pd.Series(movieName),
    "电影评分": pd.Series(rating),
}

frame = pd.DataFrame(data)

frame.to_excel(r'F:\\爬虫实验\\豆瓣爬虫试验\\豆瓣迪电影TOP250.xlsx')
