#京东商城评论爬取
import requests
import os
import json
import time
import csv
#from bs4 import BeautifulSoup
url = 'https://club.jd.com/comment/productPageComments.action'
#声明爬虫访问网站时所使用的浏览器身份
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    #cookie
    'Cookie':'此处需要手动填入'
}
data= {
'callback':'', #'callback':'fetchJSON_comment98'
'productId':'234431',
'score':'0',
'sortType':'5',
'page':'0',
'pageSize':'10',
'isShadowSku':'0',
'fold':'1'
}
#txt 文件
f = open("data.txt", 'w', encoding='utf-8')
#对 page1-10 遍历 更改 page 然后更改 data 的传入
for index in range(100):
    print("page ", index)
    data['page'] = index
    r = requests.get(url=url, headers=headers, params=data)
    #存入：nickname, productColor, content
    for comment in r.json()['comments']:
        c_nickname = comment['nickname']
        c_content = comment['content']
        if comment.__contains__('productColor'):
            c_color = comment['productColor']
        else:
            c_color = ''
    # single_comment_cont = [comment['content'] for comment in r.json()['comments']] #单条评论内容
    # for i in single_comment_cont:
    # print(i)
    # f.write(i)
        with open('jingdongcom.csv', 'a', newline='',encoding='utf-8') as file:
            rows = [c_nickname,c_color,c_content]
            mywriter = csv.writer(file)
            mywriter.writerow(rows)
    time.sleep(10)