import requests
from bs4 import BeautifulSoup


# получение списка ссылок на квартиры с указанной страницы
def get_links_of_flats_from_page(page):
    r = requests.get(page)

    if r.ok:
        soup = BeautifulSoup(r.text, 'lxml')
    else:
        print('Bad request')

    lst = (soup.findAll('a', class_="c6e8ba5398--header--1fV2A"))

    list_of_links_from_page = []

    print(len(lst))

    for i in lst:
        print('link is :', i.attrs['href'])
        list_of_links_from_page.append(i.attrs['href'])

    print(len(list_of_links_from_page))
    # print(lst[0].attrs['href'])
    # print(lst[1].attrs['href'])

    return list_of_links_from_page


