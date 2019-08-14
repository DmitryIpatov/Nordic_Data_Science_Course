import src.selenium_test as st
import src.parser as p
import src.flat


#page = 'https://www.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'

#page = "http://www.python.org"
#st.execute(page=page)



page = 'https://www.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'

links_of_flats_from_page = p.get_links_of_flats_from_page(page)

print(links_of_flats_from_page[0])

flat = src.flat.Flat()

#link = 'https://www.cian.ru/sale/flat/212633712/'
#
flat.get_content(links_of_flats_from_page[0]) #this is 'https://www.cian.ru/sale/flat/212633712/'
#
print('Метро: ', flat.metro)

