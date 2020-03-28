import bs4
import re
import requests
import random

UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

ua = UAS[random.randrange(len(UAS))]

headers = {'user-agent': ua}


with open('swiss-urls.txt') as f:
  lineList = f.readlines()

for links in lineList:
    r = requests.get(links)
    data = r.text


    searched_word = ['Corona', 'Schweden', 'University', 'exam', 'exams']

    for keywords in searched_word:
        soup = bs4.BeautifulSoup(data, 'html.parser')
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(keywords)), recursive=True)

        print('Found the word "{0}" {1} times\n'.format(keywords, len(results)))

        for content in results:
            words = content.split()
            for index, word in enumerate(words):
                # If the content contains the search word twice or more this will fire for each occurence
                if word == keywords:
                    print('Whole content: "{0}"'.format(content))
