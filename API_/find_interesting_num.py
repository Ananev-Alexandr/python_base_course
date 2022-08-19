import requests


with open('test.txt') as f:
    line = f.read().splitlines()
    for i in line:
        api_url = f"http://numbersapi.com/{i}/math?json=true"
        res = requests.get(api_url)
        data = res.json()
        if data['found'] is True:
            print('Interesting')
        else:
            print('Boring')