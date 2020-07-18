import urllib.request

print('测试代理IP的小程序')

url = 'http://myip.kkcha.com'

proxy_support = urllib.request.ProxyHandler({'http':'221.130.17.153:80'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362')]

urllib.request.install_opener(opener)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')

print(html)
