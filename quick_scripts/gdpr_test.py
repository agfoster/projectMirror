import codecs
import requests
from multiprocessing.dummy import Pool as ThreadPool

mightyFile = open('majestic_million.csv', encoding='UTF-8')
mightyMil = mightyFile.read().splitlines()
mightyMil = mightyMil[1:10001]
mightyFile.close()


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


domains = []
for line in mightyMil:
    domains.append(line.split(',')[2])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
count = 0
totalStats = []


def checker(domainIn):
    global count
    global totalStats
    count = count + 1
    if count % 100 == 0:
        printProgressBar(count, 10000)
    try:
        req = requests.get("http://" + domainIn, timeout=5, headers=headers)
        stat = req.status_code
    except:
        try:
            req = requests.get("http://www." + domainIn, timeout=5, headers=headers)
            stat = req.status_code
        except:
            stat = "failed"
    totalStats.append((domainIn, stat))
    return (domainIn, stat)

pool = ThreadPool(10)
pool.map(checker, domains)
pool.close()
pool.join()

with open('gdprSucks.csv', 'a', encoding='utf-8') as outfile:
    for stat in totalStats:
        outFile.write(str(stat[0]) + ',' + str(stat[1]) + '\n')
