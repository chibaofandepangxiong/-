import requests
import re
import os
if not os.path.exists('./qiushitupian'):
    os.mkdir('./qiushitupian')
headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'
}
url = 'https://www.qiushibaike.com/imgrank/page/%d/'
for pageNnm in range(1,3):
    new_url = format(url%pageNnm)
    shu_ju = requests.get(url=url,headers=headers).text #使用通用爬虫对url一整张页面爬取
    jie_xi = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  #焦距爬虫正则
    #<div class="thumb"
    # <a href="/article/124169009" target="_blank">
    # <img src="//pic.qiushibaike.com/system/pictures/12416/124169009/medium/FH716893PTRAIUL5.jpg" alt="糗事#124169009" class="illustration" width="100%" height="auto">
    # </a>
    # </div>'
    pi_pei = re.findall(jie_xi,shu_ju,re.S)
    # print(pi_pei)
    for src in pi_pei:
        src = 'https:'+src
        img_data = requests.get(url=src,headers=headers).content  #text()返回字符串，content()返回二进制，json()返回对象
        img_name =src.split('/')[-1]
        imgPath = './qiushitupian/'+img_name
        with open(imgPath,"wb") as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！')


