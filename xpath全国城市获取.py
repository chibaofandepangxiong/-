import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36"
    }
    url = 'https://www.aqistudy.cn/historydata/'
    huo_qu = requests.get(url=url,headers=headers).text

    tree = etree.HTML(huo_qu)
    host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    print(host_li_list)
    all_city_names = []
    #热门城市名称
    for li in host_li_list:
        host_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(host_city_name)
    #解析的是全部城市的名称
    city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_names_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))

    