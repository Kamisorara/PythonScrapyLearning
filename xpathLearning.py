# -*- coding: utf-8 -*-
from lxml import etree
import requests

# URL = "https://movie.douban.com/top250" #豆瓣

URL = "https://movie.douban.com/explore"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
requestResult = requests.get(url=URL, headers=headers)

htmlText = requestResult.text

webHtml = etree.HTML(htmlText)
item = webHtml.xpath('//*[@id="app"]/div/div[2]/ul/li/a/div/div/div/div/span[@class="drc-subject-info-title-text"]/text()')
# item = webHtml.xpath('//ol/li/div[@class="item"]/./div[@class="info"]/div[@class="hd"]/a/span[1]/text()') #豆瓣250

print(htmlText)
