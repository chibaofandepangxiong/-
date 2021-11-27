import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers= {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'
}
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    shu_ju =requests.get(url=url,headers=headers)
    shu_ju.encoding='UTF-8'
    xin_shu_ju =shu_ju.text

    spou = BeautifulSoup(xin_shu_ju,'lxml')
    list_li = spou.select('.book-mulu > ul> li')
    fp = open('./sanguo.txt','w',encoding='UTF-8')
    for li in list_li:
        title = li.a.string
        xiang_qing_url = 'https://www.shicimingju.com'+li.a['href']
        xiang_shu_ju=requests.get(url=xiang_qing_url,headers=headers)
        xiang_shu_ju.encoding='UTF-8'
        xin_xiang_qing = xiang_shu_ju.text
        deta_suop = BeautifulSoup(xin_xiang_qing,'lxml')
        div_data = deta_suop.find('div',class_='chapter_content')
        huo_qu = div_data.text
        fp.write(title+':'+huo_qu+'\n')
        print(title,'获取成功')



