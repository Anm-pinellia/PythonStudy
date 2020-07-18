import urllib.request
import urllib.parse
import json

print('中英文翻译测试')
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

while True:
    word=input('请输入需要翻译的内容:\n')
    data={  'type': "AUTO",
            'i': word,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
                }


    data=urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    result=target['translateResult'][0][0]['tgt']

    print('翻译结果:\n',result,'\n')
