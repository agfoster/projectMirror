import requests
import time
import random
import re

# An investigation required visiting a domain multiple times to see where it redirected to

results = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

#redirection domain here
domain = ''

for x in range(1,500):

    delay = random.randint(0,10)

    time.sleep(10 + delay)
    data = requests.get(domain, headers=headers)

    with open('siphonResults.txt', 'a', encoding='UTF-8') as results:
        results.write(str(data.headers) + "\n")

    print(data.headers)
