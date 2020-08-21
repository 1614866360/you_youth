#-*- coding:utf-8 -*-
#@Time :  0:44
#@Author: Thomas
#@File :script.py
#@Software : PyCharm

import json
import time
from bs4 import BeautifulSoup
import re
import requests
import random

#headers
headers={
    'Cookie':'BDqhfp=%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%9B%BE%E7%89%87%E7%94%9F%E6%B4%BB%E7%85%A7%26%26NaN-1undefined-1undefined%26%261081%26%262; BIDUPSID=A3705FA29010F89F7B00E44FB47584C8; PSTM=1572235160; BAIDUID=A3705FA29010F89F5136D170EDB3D5CC:FG=1; indexPageSugList=%5B%22%E5%8F%B2%E8%92%82%E8%8A%AC%E6%88%90%E5%8A%9F%22%5D; BDUSS=HFoTWtXNVE5a1hUNGdaMzJGVlAwRkJESENPZG9rMWxlVFpXUlhoYmhsc1J0RTFmSVFBQUFBJCQAAAAAAAAAAAEAAADJe6b1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEnJl8RJyZfN; BDUSS_BFESS=HFoTWtXNVE5a1hUNGdaMzJGVlAwRkJESENPZG9rMWxlVFpXUlhoYmhsc1J0RTFmSVFBQUFBJCQAAAAAAAAAAAEAAADJe6b1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEnJl8RJyZfN; MCITY=-161%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; ZD_ENTRY=baidu; H_PS_PSSID=1455_32439_32531_32046_32117_32499_32482; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
    'Host': 'image.baidu.com',
    'Referer':'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs3&word=%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%9B%BE%E7%89%87%E7%94%9F%E6%B4%BB%E7%85%A7&oriquery=%E8%99%9E%E4%B9%A6%E6%AC%A3%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87&ofr=%E8%99%9E%E4%B9%A6%E6%AC%A3%E9%AB%98%E6%B8%85%E5%9B%BE%E7%89%87&hs=2&sensitive=0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    "X-Requested-With": "XMLHttpRequest"

}
n=0
for i in range(0,10):
    sleep_time=random.randint(0,2)
    time.sleep(sleep_time)
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%9B%BE%E7%89%87%E7%94%9F%E6%B4%BB%E7%85%A7&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E8%99%9E%E4%B9%A6%E6%AC%A3%E5%9B%BE%E7%89%87%E7%94%9F%E6%B4%BB%E7%85%A7&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn='+str(i*30)+'&rn=30'
    response=requests.get(url,headers=headers)
    a=response.text
    r=re.compile(r'"thumbURL":"(.*?)"')
    url_reals=re.findall(r,a)
    for i in url_reals:
        item=requests.get(i).content
        n += 1
        file_path='D:\\19001837\\python\\project\\yu\\picture'+str(n)+'.jpg'
        train_path='D:\\19001837\\python\\project\\train_list.TXT'
        validate_path='D:\\19001837\\python\\project\\validate.TXT'
        test_path='D:\\19001837\\python\\project\\test_list.TXT'
        with open(file_path,'wb+') as f:
            f.write(item)
            f.close()
            if n <= 240:
                with open(train_path,'a+') as op:
                    name_list='yu/picture'+str(n)+'.jpg 0'
                    op.write(name_list+'\n')
                    op.close()
            elif 240<n<=270:
                with open(validate_path,'a+') as vp:
                    validate='yu/picture'+str(n)+'.jpg 0'
                    vp.write(validate+'\n')
                    vp.close()
            else:
                with open(test_path,'a+') as tp:
                    test='yu/picture'+str(n)+'.jpg 0'
                    tp.write(test+'\n')
                    tp.close()

            print('第%d张图片'%n)
            print(i)









