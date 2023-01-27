import urllib.request
#n = 0
#while 1:
#    n=n+1
#    response = urllib.request.urlopen('https://web.archive.org/web/20230114112630/https://jikipedia.com/definition/')
#    print(response.read().decode('utf-8'))
import pandas as pd

error = []
df = pd.read_csv("file.csv")
#response = urllib.request.urlopen('https://wuyuan.dev').read().decode('utf-8')
#print(response)
for i in range(30321):
    try:
        s = str(i)
        print('正在保存第'+s+'行')
        url = df['original'][i]
        print(url)
        response = urllib.request.urlopen('https://web.archive.org/web/'+url).read().decode('utf-8')
        with open('/data/'+s+".html", "w" ,encoding='utf-8') as file:
            file.write(response)
        print('保存成功')
    except:
        print('第'+s+'行出错')
        error.append(s)
        pass
    
    
    