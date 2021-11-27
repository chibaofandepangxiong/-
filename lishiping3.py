import requests
from lxml import etree
from multiprocessing.dummy import Pool
import re
import random
import time
seesion=requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
}
def get_vide(dic):
    url = dic['url']
    name = dic['name']
    time.sleep(random.random())
    # print(url)
    data = seesion.get(url=url,headers=headers).content
    print(name)
    name=re.search ('[\u4E00-\u9FA5]+',name).group()
    print(name)
#     持久化
    with open('C:\\Users\\Public\\Desktop\\'+str.strip(name)+'2.mp4', 'wb') as fp:
        fp.write(data)
        print('下载成功'+name+str(len(data)))

if __name__ == '__main__':
    url = 'https://www.pearvideo.com/category_5'
    respones=seesion.get(url=url,headers=headers)
    trees = etree.HTML(respones.text)
    li_list=trees.xpath('//ul[@class="listvideo-list clearfix"]/li')
    Mp4s=[]
    i=1
    for li in li_list:
       href = li.xpath('./div[1]/a[1]/@href')
       text = li.xpath('./div/a/div[2]/text()')[0]
       # 视频的id
       vide_id=re.sub('video_','',href[0])
       # print(vide_id)


       # 拿到视频的链接 放在头请求中
       href = 'https://www.pearvideo.com/'+href[0]



       # ajax请求获取到视频地址
       url='https://www.pearvideo.com/videoStatus.jsp'
       params= {
           'mrd': '0.08621106931553091',
           'contId': str.strip(vide_id)
       }
       headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
           'Referer': href
       }
       respones= seesion.get(url=url,headers=headers,params=params)
       json_text=respones.json()
       # 这里的视频地址和图片地址是 假的，要分开组合成真正的视频地址
       mp4_jpg=json_text['videoInfo']['video_image']
       mp4_url=json_text['videoInfo']['videos']['srcUrl']

       # 瞎几把拼接出真实的视频地址
       c=str(mp4_jpg).split('/')[5][0:-13]
       mp4_url=re.sub('/(\d*)-','/'+c+'-',mp4_url)

       # 把视频url和名称添加到列表中
       dic={
           'url': mp4_url,
           'name': text
       }
       headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
       }
       # url和视频名称加到数组中
       Mp4s.append(dic)
    # 初始化一个线程池
    pool = Pool(len(Mp4s))
    pool.map(get_vide,Mp4s)
