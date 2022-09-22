# -*- coding: utf-8 -*-
import time

from lxml import etree
import requests
import pandas as pd

URL = "https://huoche.8684.cn/sitemap"
# 添加请求头以防万一
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

htmlText = requests.get(url=URL, headers=headers).text

tree = etree.HTML(htmlText)

trains = tree.xpath('/html/body/div[5]/div[2]/div[1]/div[@class="blocklist mt20"]/div[2]/a/text()')  # 获取所有高铁组班号

for train in trains:  # 获取当日所有高铁班车行程
    try:
        URL_DETAIL = "https://huoche.8684.cn/h_" + train
        requestResult = requests.get(url=URL_DETAIL, headers=headers)

        DetailHtmlText = requestResult.text

        webHtml = etree.HTML(DetailHtmlText)

        item = webHtml.xpath('/html/body/div[5]/div[3]/div[1]/div[1]')

        # 获取头部
        head = item[0].xpath('//table/thead/tr/th/text()')

        # 获取站次
        stationNum = item[0].xpath('//table/tbody/tr/td[1]/text()')

        # 获取站点
        stationName = item[0].xpath(
            '//table/tbody/tr/td/a[@class="site_name"]/text()')

        # 获取日期
        date = item[0].xpath('//table/tbody/tr/td[1]/text()')

        # 获取到达时间
        arriveTime = item[0].xpath('//table/tbody/tr/td[4]/text()')

        # 离开时间
        leaveTime = item[0].xpath('//table/tbody/tr/td[5]/text()')

        # 停留时间
        remainTime = item[0].xpath('//table/tbody/tr/td[6]/text()')

        # 里程
        mileage = item[0].xpath('//table/tbody/tr/td[7]/text()')

        data = {
            head[0]: pd.Series(stationNum),
            head[1]: pd.Series(stationName),
            head[2]: pd.Series(date),
            head[3]: pd.Series(arriveTime),
            head[4]: pd.Series(leaveTime),
            head[5]: pd.Series(remainTime),
            head[6]: pd.Series(mileage)
        }

        resultForm = pd.DataFrame(data)

        resultForm.to_excel(train + "火车出发时刻表.xlsx")  # 保存成excel
        # print(resultForm)
        print(train + "打印完成")
    except Exception as e:
        print(train + "无车次")
    time.sleep(0.5)  # 一秒请求两次防止阈值过高
