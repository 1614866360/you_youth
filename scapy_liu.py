# -*- coding: utf-8 -*-
# @File  : scapy_liu.py
# @Author: Thomas_yx
# @Date  : 2020/8/20
# @Contact : yx20001210@163.com
# @Software : PyCharm


import json
import re
import requests
import time
import random
from bs4 import BeautifulSoup

headers={
    'Cookie':'BDqhfp=%25D0%25ED%25BC%25D1%25E7%25F7%26%26NaN-1undefined%26%260%26%261; BIDUPSID=A3705FA29010F89F7B00E44FB47584C8; PSTM=1572235160; BAIDUID=A3705FA29010F89F5136D170EDB3D5CC:FG=1; indexPageSugList=%5B%22%E5%8F%B2%E8%92%82%E8%8A%AC%E6%88%90%E5%8A%9F%22%5D; BDUSS=HFoTWtXNVE5a1hUNGdaMzJGVlAwRkJESENPZG9rMWxlVFpXUlhoYmhsc1J0RTFmSVFBQUFBJCQAAAAAAAAAAAEAAADJe6b1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEnJl8RJyZfN; BDUSS_BFESS=HFoTWtXNVE5a1hUNGdaMzJGVlAwRkJESENPZG9rMWxlVFpXUlhoYmhsc1J0RTFmSVFBQUFBJCQAAAAAAAAAAAEAAADJe6b1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEnJl8RJyZfN; MCITY=-161%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ai-studio-ticket=43BC917DC0744DE2B0F13FE17D5460B5B9845E3AEF284114AEE7255716C65C78; H_PS_PSSID=1455_32439_32533_32046_32117_32499_32481; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
    'Referer':'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D0%ED%BC%D1%E7%F7&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111',
    'Host':'image.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

}
n=0
for i in range(0,10):
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%88%98%E9%9B%A8%E6%98%95&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E5%88%98%E9%9B%A8%E6%98%95&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn='+str(i)+'&rn=30'
    response=requests.get(url,headers=headers).text
    # print(response)
    r=re.compile(r'"thumbURL":"(.*?)"')
    url_real=re.findall(r,response)
    for item in url_real:
        n+=1
        print("————第%d张图片正在下载————"%n)
        print(item)
        file_path='D:\\19001837\\python\\project\\liu\\picture'+str(n)+'.jpg'
        train_path = 'D:\\19001837\\python\\project\\train_list.TXT'
        validate_path='D:\\19001837\\python\\project\\validate.TXT'
        test_path='D:\\19001837\\python\\project\\test_list.TXT'
        with open(file_path,'wb+') as f:
            i=requests.get(item).content
            f.write(i)
            f.close()
            if n<=240:
                with open(train_path,'a+') as op:
                    name_list='liu/picture'+str(n)+'.jpg 2'
                    op.write(name_list+'\n')
                    op.close()
            elif 240<n<=270:
                with open(validate_path,'a+') as vp:
                    validate='liu/picture'+str(n)+'.jpg 2'
                    vp.write(validate+'\n')
                    vp.close()
            else:
                with open(test_path,'a+') as tp:
                    test='liu/picture'+str(n)+'.jpg 2'
                    tp.write(test+'\n')
                    tp.close()




