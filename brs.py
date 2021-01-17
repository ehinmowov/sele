import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.64 Safari/537.36'}

page = 'https://boston.craigslist.org/search/sof'

response = requests.get(page, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

this = soup.find_all('a', class_ = 'result-title hdrlnk', href=True)
for i in this:
    job_title = i.get_text()
    links = i['href']
    print(f'\n Job: {job_title} \n URL: {links}')


