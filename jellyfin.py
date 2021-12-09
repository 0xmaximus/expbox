import requests,sys
requests.packages.urllib3.disable_warnings()

urlListPath=sys.argv[1] 
if '.txt' in urlListPath:
    urlList = open(urlListPath, 'r',encoding='utf-8')
else:
    urlList = [urlListPath]
for url in urlList:
    url=url.strip()+"/Images/Remote?imageUrl=http://www.google.com"
    heads={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",}
    try:
        req=requests.get(url,headers=heads)
        if "baidu.com" in req.text:
            print(url+"hava vul")
        else:
            print(url+"no vul")
    except Exception as e:
        print(e)
