import re

results = []

with open('siphonResults.txt', 'r', encoding='UTF-8') as results:
    results = results.readlines()

    for x in results:
        for y in re.split('; |, ', x):
            if y.find('domain=') >= 0:
                if y.split('=')[1] not in results:
                    results.append(y.split('=')[1])
                    print(y.split('=')[1])
