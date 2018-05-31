import codecs
import requests
import progressbar
from multiprocessing.dummy import Pool as ThreadPool 

mightyFile = open('majestic_million.csv')
mightyMil = mightyFile.read().splitlines()
mightyMil=mightyMil[1:]

domains = []
for line in mightyMil:
	domains.append(line.split(',')[2])
	
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
count = 0
totalStats = []
bar = progressbar.progressbar(range(10000))
def checker(domainIn):
	global count
	global totalStats
	count = count + 1
	if (count % 100) == 0:
		bar.next()
		outFile = codecs.open('gdprSucks.csv', 'a', encoding='utf-8')
		for stat in totalStats:
			outFile.write(str(stat[0])+','+str(stat[1])+'\n')
		outFile.close()
	totalStats = []
	try:
		req = requests.get("http://"+domainIn, headers=headers)
		stat = req.status_code
	except:
		try:
			req = requests.get( "http://www."+domainIn, headers=headers)
			stat = req.status_code
		except:
			stat = "failed"
	totalStats.append((domainIn,stat))
	return (domainIn,stat)
	
pool = ThreadPool(10) 
pool.map(checker, domains)
pool.close() 
pool.join() 
