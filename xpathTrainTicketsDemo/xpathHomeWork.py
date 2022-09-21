# -*- coding: utf-8 -*-
from lxml import etree
import requests
import pandas

# 最终结果
#     站次  站名     日期 到达时间 开车时间 停留时间  里程
# 0    1   北京南站   1  06:43  06:43   --     0公里
# 1    2   沧州西站   2  07:35  07:38   3分   210公里
# 2    3   德州东站   3  08:05  08:13   8分   314公里
# 3    4   济南西站   4  08:37  08:41   4分   406公里
# 4    5    泰安站   5  08:58  09:00   2分   465公里
# 5    6    枣庄站   6  09:38  09:40   2分   627公里
# 6    7   宿州东站   7  10:12  10:14   2分   760公里
# 7    8   南京南站   8  11:14  11:16   2分  1023公里
# 8    9   镇江南站   9  11:35  11:37   2分  1088公里
# 9   10   苏州北站  10  12:13  12:15   2分  1237公里
# 10  11  上海虹桥站  11  12:40  12:40   --  1318公里
# ===========================================================================
URL = "http://huoche.8684.cn/h_G101"
# 添加请求头以防万一
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

requestResult = requests.get(url=URL, headers=headers)

htmlText = requestResult.text

webHtml = etree.HTML(htmlText)

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
    head[0]: pandas.Series(stationNum),
    head[1]: pandas.Series(stationName),
    head[2]: pandas.Series(date),
    head[3]: pandas.Series(arriveTime),
    head[4]: pandas.Series(leaveTime),
    head[5]: pandas.Series(remainTime),
    head[6]: pandas.Series(mileage)
}

resultForm = pandas.DataFrame(data)

resultForm.to_excel("火车出发时刻表.xlsx")  # 保存成excel

print(resultForm)
