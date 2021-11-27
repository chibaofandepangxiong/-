import requests
from lxml import etree
import os
#缺点收缩图
if not os.path.exists('./4ktupian'):
    os.mkdir('./4ktupian')
if __name__ == '__main__':
    headers={
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36"
  }
    url = 'https://pic.netbian.com/4kmeinv/'
    tu_pain = requests.get(url=url,headers=headers)
    # tu_pain.encoding = 'utf-8'
    xin_tu_pian = tu_pain.text
    #数据解析：src的属性值 alt属性值
    shi_li = etree.HTML(xin_tu_pian)
    jie_xi= shi_li.xpath('//div[@class="slist"]/ul/li')
    # print(jie_xi)
    for so in jie_xi:
        scr_jie_xi = 'https://pic.netbian.com'+so.xpath('./a/img/@src')[0]
        alt_name = so.xpath('./a/img/@alt')[0]+'.jpg'
        alt_name = alt_name.encode('iso-8859-1').decode('gbk')#转换编码为iso-8859-1，再用decode解码为gbk格式
        img_data = requests.get(url=scr_jie_xi,headers=headers).content
        img_name = '4ktupian/'+alt_name
        with open(img_name,'wb') as fp:
            fp.write(img_data)
            print(alt_name,"成功！！")

