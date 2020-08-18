import urllib.request

want=input('请输入你想要猫猫图片大小(格式为a/b):\n')
reponse=urllib.request.urlopen('http://placekitten.com/'+str(want))
cat_img=reponse.read()

with open('E:\\实验截图\cat1.jpg','wb') as cat:
    cat.write(cat_img)
    
    
