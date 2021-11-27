import requests
from lxml import etree
import random
from multiprocessing import Pool
import re
session=requests.Session()
headers={
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36"

}
url='https://www.pearvideo.com/category_5'
sheng_huo = session.get(url=url,headers=headers).text
lp = etree.HTML(sheng_huo)
li_list = lp.xpath('//*[@id="listvideoListUl"]/li')
# print(li_list)
urls=[]
for paqu in li_list:
    deta_url = 'https://www.pearvideo.com/'+paqu.xpath('./div/a/@href')[0]
    # print(deta_url)
    name = paqu.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    #对详情页发起请求和获取响应数据
    xiang_qing = session.get(url=deta_url,headers=headers).text
    #从上一步中解析出视屏的地址，如返回为空，则为动态加载，需查找真实地址
    # print(xiang_qing)


    contId= deta_url[::-1][:7][::-1]
    # print(contId)
    zheng_shi_url = 'https://www.pearvideo.com/videoStatus.jsp'
    # print(zi_dian)
    headers1 = {
        'Referer': deta_url,
        'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36"

    }
    zi_dian ={
        'mrd':str(random.random()),
        'contId ':str.strip(contId)

    }
    # print(zi_dian)
    respones = session.get(url=zheng_shi_url,headers=headers1,params=zi_dian).json()
    mp4_jpg = respones['videoInfo']['video_image']
    mp4_url = respones['videoInfo']['videos']['srcUrl']

    # 拼接出真实的视频地址
    c = str(mp4_jpg).split('/')[5][0:-13]
    mp4_url = re.sub('/(\d*)-', '/' + c + '-', mp4_url)

    # print(video_url)
    dic = {
        'url': mp4_url,
        'name': name
    }
    urls.append(dic)
#持久存储
def get_viode_data(dic):
    url =dic['url']
    print(dic['name'],'正在下载.....')
    data = requests.get(url=url,headers=headers).content
    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功！')

#线程池
pool=Pool(4)
pool.map(get_viode_data,urls)
pool.close()
pool.join()
