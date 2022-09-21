# -*- coding: utf-8 -*-
# 55122105636 吴逸风
import requests
import urllib3

DESK_TOP_PATH = "C:\\Users\\12102\\Desktop\\爬虫作业第三周作业\\"  # 新创建的txt文件的存放路径 (桌面路径)
REQUEST_URL = "http://laf.kamisora.xyz"
GET = "GET"
POST = "POST"


# requests获取请求地址
def getRequest(fileName, url):
    filePath = DESK_TOP_PATH + fileName + '.txt'  # 也可以创建一个.doc的word文档
    result = requests.get(url)  # 可以直接调用 get | post  方法
    file = open(filePath, 'w+', encoding="utf-8")
    file.write(result.text)
    file.close()
    print(result.text)


# urllib3 获取
def getRequestByUrllib3(fileName, url, requestMethod):
    poolmanager = urllib3.PoolManager()  # 获取连接池对象
    filePath = DESK_TOP_PATH + fileName + '.txt'  # 也可以创建一个.doc的word文档
    resultTemp = poolmanager.request(requestMethod, url)
    result = resultTemp.data.decode()  # 中文解码
    file = open(filePath, 'w+', encoding="utf-8")
    file.write(result)
    print(result)


if __name__ == "__main__":
    getRequest("MOOCHtml", REQUEST_URL)  # requests Method
    getRequestByUrllib3("Urllib3RequestResponse", REQUEST_URL, GET)
