import requests
import os

def Cookie():
    url = 'https://www.douban.com'
    HttpHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    HttpHost = 'www.douban.com'
    cookie = 'll="108288"; bid=xtSWohYOuao; _pk_id.100001.8cb4=97696c4ff85a2202.1623338187.1.1623338187.1623338187.; _pk_ses.100001.8cb4=*; __utma=30149280.550186300.1623338187.1623338187.1623338187.1; __utmb=30149280.2.9.1623338187; __utmc=30149280; __utmz=30149280.1623338187.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1'
    cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    cookie2 = 'll="108288"; bid=xtSWohYOuao; _pk_id.100001.8cb4=97696c4ff85a2202.1623338187.2.1623388522.1623338201.; __utma=30149280.550186300.1623338187.1623338187.1623338187.1; __utmc=30149280; __utmz=30149280.1623338187.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2="162072674:AHmNPe82zgw"; ck=USsq; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1623388522%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __gads=ID=fe8d755a0fc3a144-220f1c0e62c900e7:T=1623388529:S=ALNI_MZxBRg3zSIn4TcPcJv9_vFPKHKHFQ'
    cookie_dict2 = {i.split("=")[0]: i.split("=")[-1] for i in cookie2.split("; ")}
    respose = requests.get(url,headers = HttpHeaders,cookies = cookie_dict)
    with open(os.getcwd()+'\\test1.txt','w',encoding='utf-8') as f1:
        f1.write(respose.text)
    respose2 = requests.get(url,headers = HttpHeaders,cookies = cookie_dict2)
    with open(os.getcwd()+'\\test2.txt','w',encoding='utf-8') as f2:
        f2.write(respose2.text)

if __name__ == '__main__':
    Cookie()