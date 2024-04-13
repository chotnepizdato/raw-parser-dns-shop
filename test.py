from time import sleep as pause
import undetected_chromedriver as uc
from bs4 import BeautifulSoup as BS

driver = uc.Chrome()

catalog = ['https://www.dns-shop.ru/catalog/8ccf9d205ab44e77/tarify-operatorov/',
           "https://www.dns-shop.ru/catalog/04b0910177f4b2db/sterzhni-dlya-stilusov/",
           "https://www.dns-shop.ru/catalog/recipe/3efd93fe8c3bcfc3/antivirusy/",
           "https://www.dns-shop.ru/catalog/aab9cdea473f61ef/sim-adaptery/",
           "https://www.dns-shop.ru/catalog/17a90cea16404e77/radiostancii/"]


def get_description(url):
    driver.get(url)
    pause(10)
    product_soup = BS(driver.page_source, 'lxml')

    name = product_soup.find('div', class_='product-card-top__name').text
    offer = product_soup.find('div', class_='product-card__offer').text

    product_link = url
    description = product_soup.find('div', class_='product-card-description-text').text
    print('-'*40)
    print(name, '\n', offer.strip(), '\n', product_link, '\n', description)

    category = product_soup.find_all('span')
    for i in category:
        if bool(str(i).find('data-go-back-catalog') != -1):
            category = i.text
        else:
            continue


def get_links():
    category_soup = BS(driver.page_source, 'lxml')
    things = category_soup.find_all('a', class_="catalog-product__name ui-link ui-link_black")
    links = map(lambda thing: 'https://www.dns-shop.ru' + thing.get("href"), things)

    for link in links:
        get_description(link)


for index, category in enumerate(catalog):
    index += 1
    driver.get(category)
    print('='*40)
    print(f'Searching for products in category №{index}')
    pause(5)
    get_links()
