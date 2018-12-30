import requests, json, sqlite3, logging
from time import sleep

def queryDict(word_id, attempt=0):

    if attempt >= 5:
        raise Exception('Too many attempts querying dictionary, check logs.')

    sleep(5)

    app_id = '917f60de'
    app_key = '5b293fcef7bb9a2e2e8277fd14e7a58b'

    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    if r.status_code == 200:

        logging.debug('Returned %s on %s' % (r.status_code, word_id))
        return(r.json())

    else:
        attempt = attempt + 1
        logging.warning('Failed to receive a 200 from the Dictionary API, re-attempt # %s' % attempt)
        queryDict(word_id,attempt)



def testJson():

    with open('response.json', 'r+') as file:

        logging.debug('Loading local file...')
        test = json.loads(file.readlines())

        logging.debug('Local file successfully loaded as JSON...')

        for each in test['results'][0]['lexicalEntries']:
            print(each['lexicalCategory'])

def main():

    #settup sqlite3 datbase

    logging.basicConfig(level=logging.DEBUG)

    logging.debug('Script Start')



    with open('wordList.txt', 'r') as wordList:
        logging.debug('wordList.txt successfully opened')

        wordsWithType = {}


        for word_id in wordList.read():

            logging.debug('looping over word list ')
            results = queryDict(word_id)

            lexicalCategory = []

            for each in results['results'][0]['lexicalEntries']:
                print('Discovered that ' + word_id + 'is a ' + each['lexicalEntries'] + '!')
                lexicalCategory.append(each['lexicalEntries'])

            wordsWithType[word_id] = lexicalCategory

        with open('result.json', 'w') as fp:
            logging.debug('attempting to save results')
            json.dump(wordsWithType, fp)
            logging.debug('results should be saved')

main()