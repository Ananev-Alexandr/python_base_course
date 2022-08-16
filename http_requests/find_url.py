from requests import get
from re import findall


url1 = input()
url2 = input()
result = 'No'


def find_true_url(url):
    res = get(url)
    regular = findall(r'href="(.*)"', res.text)
    if regular == []:
        return False
    return regular


try:
    for new_url in find_true_url(url1):
        if find_true_url(url1) is False:
            break
        if url2 in find_true_url(new_url):
            result = ('Yes')
    print(result)
except:
    print("No")
