import time
import csv
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

BASE_URL = 'https://coinmarketcap.com/ru/'
# BASE_URL = requests.get('https://coinmarketcap.com/ru/')

def get_html(url):
    # req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
    # response = urlopen(req).read()
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollBy(0, window.innerHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    return driver.page_source


def parse_url(html):

    crypts_dict = []
    names_list = []
    values_list = []
    percent_list = []
    all_values = 0

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('tbody')
    list_of_names = table.find_all('p', {'class': 'sc-4984dd93-0 kKpPOn'})
    list_of_values = table.find_all('span', {'class': 'sc-7bc56c81-1 bCdPBp'})


    for names, values in zip(list_of_names, list_of_values):
        name = names.text[0: + names.text.find(" ")]
        names_list.append(name)

        value = values.text[1:]
        values_list.append(value)

        crypt_dict = {'Name': name, 'MC': value}
        crypts_dict.append(crypt_dict)

        all_values += int(values.text[1:].replace(',', ''))
        # print(name, value)
    # print(names_list)

    a = 0
    for value in values_list:
        percent = int(value.replace(',', '')) / (all_values / 100)
        percent_list.append(str(format(percent, '.2f')) + '%')
        crypts_dict[a]['MP'] = str(format(percent, '.2f')) + '%'
        a += 1

    return crypts_dict
    # print(all_values)
    # print(names_list)
    # print(values_list)
    # print(percent_list)
    # print(crypts_dict)

def save_url(crypts_dict,path):
    with open(path,'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=crypts_dict[0])
        writer.writeheader()
        writer.writerows(crypts_dict)

def main():
    all_url = parse_url(get_html(BASE_URL))
    save_url(all_url, f'{datetime.datetime.now().strftime("%H.%M_%d.%m.%Y")}.csv')
if __name__ == '__main__':
    main()