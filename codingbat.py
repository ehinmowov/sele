import requests
from bs4 import BeautifulSoup

main_page = 'https://codingbat.com/python'
sub_page = 'https://codingbat.com/'
header = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.64 Safari/537.36'}
response = requests.get(main_page, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

segment = soup.find_all('span', class_='h2')
next_page_links = []
for i in segment:
    next_page = main_page + '/' + i.get_text()
    next_page_links.append(next_page)

final_links_list = []
for links in next_page_links:
    header = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.64 Safari/537.36'}
    inner_response = requests.get(links, headers=header)
    inner_soup = BeautifulSoup(inner_response.content, 'lxml')

    question_page = inner_soup.find('div', class_='tabc')
    table = question_page.table.find_all('td')
    for those in table:
        l2 = those.find('a')['href']
        final_link = sub_page + l2
        final_links_list.append(final_link)

for f_links in final_links_list:
    header = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.64 Safari/537.36'}
    last_response = requests.get(f_links, headers=header)
    inner_soup = BeautifulSoup(last_response.content, 'lxml')

    question = inner_soup.find('p', class_='max2').get_text()
    example = inner_soup.find('td', valign='top').br
    print(example)
