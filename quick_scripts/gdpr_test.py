import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


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


print('Downloading Majestic Million, this will take some time...')
mightyMo = requests.get('http://downloads.majestic.com/majestic_million.csv')
mightyMo = mightyMo.text.splitlines()

#with open('majestic_million.csv', encoding='UTF-8') as start:
#    mightyMo = start.readlines()
#   start.close()

results = open('gdprFun4.csv', 'a', encoding='UTF-8')

for index, each in enumerate(mightyMo):
    if index == 0:
        pass
    else:
        try:
            domain = "http://" + each.split(',')[2]
            test = requests.get(domain, headers=headers)
            printProgressBar(index, 1000000, '', domain)
        except:
            try:
                domain = "http://www." + each.split(',')[2]
                test = requests.get(domain, headers=headers)
                printProgressBar(index, 1000000,'',domain)
            except:
                test.status_code = "failed"
        results.write(str(each.split(',')[2]) + "," + str(test.status_code) + "\n")
        if index % 100 == 1:
            results.flush()

results.close()
