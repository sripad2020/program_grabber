from urllib.parse import  urlparse
import requests,nltk,re,heapq
from bs4 import BeautifulSoup
url='https://www.google.com/search?q='
inp=input('enter the query: ')
urls,out_put,final_links,output,last=[],[],[],[],[]
def search(inp):
    data=requests.get(url+f'{inp}').text
    soup=BeautifulSoup(data,'html.parser')
    for links in soup.find_all('a'):
        href=links.get('href')
        urls.append(href)
    for i in urls:
        clean_url =i.split('/url?q=')[1:]
        if len(clean_url) !=0 :
            out_put.append(clean_url)
    for i in out_put:
        for j in i:
            final_links.append(j)
    for j in final_links:
        if 'https://support.google.com' not in j and 'https://accounts.google.com' not in j and 'https://www.youtube.com/' not in j:
            if 'https://stackoverflow.com/' not in j:
                output.append(j)
search(inp)
for i in output:
    parse=urlparse(i)
    url = parse.path
    last_slash_index = url.rfind('/')
    sa_index = url.find('&sa')
    url_without_param = url[:sa_index]
    a='https://',parse.netloc,url_without_param
    url = ''.join(a)
    last.append(url)
print('The size of reference is  ',len(last),'pages')
print('ENTER THE OPTION: ')
print('1. new outputs ')
print('0. for exit')
def final_output(j):
    data = requests.get(j).text
    soup = BeautifulSoup(data, "html.parser")
    code_block = soup.find_all("code")
    for links in code_block:
        print(links.get_text())
        if links == "":
            df= requests.get(j).text
            soup = BeautifulSoup(df, "html.parser")
            code_block = soup.find("code")
            for links in code_block:
                print(links.get_text())
while True:
    for j in last:
        inp = int(input('> '))
        if inp==1 :
            final_output(j)