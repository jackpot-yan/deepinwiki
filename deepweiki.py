import requests
import time
import re

time1 = time.time()
exist_url = []
g_writecount = 0

def scrappy(url,depth = 1):
    global g_writecount
    try:
        header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        r = requests.get('https://en.wikipedia.org/wiki/' + url,hadders = header)
        html = r.text
    except Exception as e:
        print('downloading',url)
        print(e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list = re.findall('<a href="/wiki/[^:#=<>]*?,/a.',html)
    unipue_list = list(set(link_list) - set(exist_url))

    for eachone in unipue_list:
        g_writecount += 1
        output = 'no' + str(g_writecount) + '\t Depth:' + str(depth) + '\t' + url +'->' + eachone +'\n'
        print(output)
        with open('tit.txt','a+') as f:
            f.write(output)
            f.close()
            if depth < 2:
                scrappy(eachone,depth + 1)

scrappy('wiki')
time2 = time.time()
print('total time',time2 - time1)
