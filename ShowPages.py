import urllib.request
import scrapy
import requests
from lxml import etree

def open_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    response = requests.get(url,headers=headers)
    html_str = response.text
    html = etree.HTML(html_str)
    return html

def get_pages():
    url='https://tieba.baidu.com/p/4662647539'
    urllist = [] 
    html = open_url(url)
    sel = html
    first_find = sel.xpath('//ul/li[@class="l_pager pager_theme_4 pb_list_pager"]')[0]
    second_find = first_find.xpath('span[@class="tP"]')[0]
    second_find_result = second_find.extract()
    if len(second_find_result) != 0:
        print('该网页存在多个页码')
        third_find = sel.xpath('//ul/li[@class="l_pager pager_theme_4 pb_list_pager"]/a[text()="尾页"]/@href').extract()
        pages = third_find[0].split('=')[-1]
    else:
        pages = 1
        print('该网页只有一页')

    for k in range(1,pages):
        url_page = url + '?pn=' + str(k)
        urllist.append(url_page)  



if __name__ == '__main__':
    get_pages()
