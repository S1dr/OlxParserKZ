
import requests
from bs4 import BeautifulSoup

URL = 'https://www.olx.kz/list/q-Iphone-12/'

#функция возвращает колличество страниц. 
def extract_max_page():
    olx_site = requests.get(URL)
    olx_soup = BeautifulSoup( olx_site.text , 'html.parser')

    pages = []

    paginator = olx_soup.find_all("span", {'class': 'item fleft'})

    for page in paginator:
        pages.append(int(page.find('span').text))

    return pages[-1]





def extract_olx_items(last_page):
    
    items = []

    #for page in range(last_page):

    result = requests.get(f'{URL}?page=0')

    if result.status_code == 200:
        print('Подключение к сайту прошло успешно!')
    else:
        print('Парсер не подключился к сайту :( )')

    soup = BeautifulSoup( result.text , 'html.parser')

    results = soup.find_all('h3', {'class':'lheight22 margintop5'})

    for result in results:
        nazvaniya = (result.find('strong').text)
        price = result.find('div', {'class' : 'space inlblk rel'})
        print("название товара : ", nazvaniya)
        print("ЦЕНА : ", price)
        print('-----------------------------')


    return items
