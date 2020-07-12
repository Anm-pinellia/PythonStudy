import urllib.request
import urllib.parse
import json

print('中英文翻译测试')

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

    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    result=target['translateResult'][0][0]['tgt']

    print('翻译结果:\n',result,'\n')

