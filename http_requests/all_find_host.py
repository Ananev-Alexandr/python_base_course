import requests
import re


web_list = []
url = input()
res = requests.get(url)
regular = re.findall(r"<a.*?href=[\'\"](?:.*?://)?(\w[\w\.\-]*).*?>", res.text)
for urls in regular:
    if urls not in web_list:
        web_list.append(urls)

web_list.sort()
for host in web_list:
    print(host)
