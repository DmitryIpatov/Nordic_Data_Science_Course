import requests
from bs4 import BeautifulSoup


class Flat:
    def __init__(self):
        self.metro = ''
        self.square_meters = 0

    # получение квартиры и заполнение атрибутов
    def get_content(self, link_to_flat):

        r = requests.get(link_to_flat)

        if r.ok:
            soup = BeautifulSoup(r.text, 'lxml')
        else:
            print('Bad flat request')

        lst = (soup.findAll('a', class_="a10a3f92e9--underground_link--AzxRC"))

        #print(lst[0].text)


        self.metro=str(lst[0].text)








