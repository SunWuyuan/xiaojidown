import urllib.request
import pandas as pd
error = []
df = pd.read_csv("file.csv")
for i in range(30321):
    try:
        s = str(i)
        print('正在保存第'+s+'行')
        url = 'https://web.archive.org/web/'+str(df['timestamp'][i])+'/'+df['original'][i]
        print(url)
        response = urllib.request.urlopen(url).read().decode('utf-8')
        with open('/data/'+s+".html", "w" ,encoding='utf-8') as file:
            file.write(response)
        print('保存成功')
    except:
        print('第'+s+'行出错')
        error.append(s)
        pass
    
    
    