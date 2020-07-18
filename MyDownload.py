import urllib.request
import os

def open_url(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')
    response = urllib.request.urlopen(req)

    html = response.read()
    return html


def get_website(url):
    html = open_url(url)
    content = html
    begin = content.find('href="96284_')+9
    end = content.find('.html">2</a>',begin)

    return content[begin:end]


def get_img(url):    
    html = open_url(url)
    content = html.decode('utf-8')
    print('转码完毕')
    img_addr = []
    
    begain = content.find('" src="')
    while begain != -1:
        end = content.find('.jpg',begin,begin+255)
        if end != -1:
            img_addr.append(content[begain+5:end+4])
        else:
            end = begain+5

        begain = content.find('" src="',end)

    print('获取图片地址运行完毕')

    return img_addr

def download_img(folder,addrlist):
    for each in addrlist:
        filename = each.split('/')[-1]
        target = open_url(each)
        with open(filename,'wb') as file:
            file.write(target)
'''
def ChAddr(url,pages_num):
    begain = url.find('96284')+5
    end = url.find('.html')
    if pages_num !=0:
        result_url = url[:begain] + '_' +str(pages_num) +url[end:]
    else:
        result_url = url
        
    return result_url
'''

def download_main(folder='E://DownloadTest',pages=6):
    url='https://www.mmonly.cc/ktmh/dmmn/'
    
    os.mkdir(folder)
    os.chdir(folder)
    page_num=pages
    '''
    for i in range(pages):
        page_num -=i
        page_url = ChAddr(url,page_num)
        print('输出的url为:',page_url)
        img_addrs = get_img(page_url)
        download_img(folder,img_addrs)
    '''
    img_addrs = get_img(url)
    download_img(folder,img_addrs)
    

    print('图片下载完毕')

if __name__ == '__main__':
    download_main()
