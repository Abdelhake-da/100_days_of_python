URL_S = [
    'https://www.amazon.com/HP-Generation-i5-1135G7-Graphics-17-cn0025nr/dp/B09FXLRBFQ/ref=sr_1_7?keywords=laptop&qid'
    '=1660590418&s=computers-intl-ship&sprefix=lap%2Ccomputers-intl-ship%2C260&sr=1-7',
    'https://www.billboard.com/charts/hot-100/2000-05-02/',
    'http://secure-retreat-92358.herokuapp.com/',
    'http://orteil.dashnet.org/experiments/cookie/',
]
edge_driver_path = 'C:\edgeWebDriver\msedgedriver.exe'
"""
from selenium import webdriver

driver = webdriver.Edge(executable_path=edge_driver_path)
driver.get(URL_S[2])
# song_name = driver.find_elements_by_css_selector('.o-chart-results-list__item h3')
# # song_name = driver.find_elements_by_css_selector('.lrv-u-width-100p li h3')
# print(len(song_name))
# for song in song_name:
#     if song.text != '':
#         print(song.text)
# driver.close()
import time
fname = driver.find_element_by_name('fName')
lname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
button = driver.find_element_by_xpath('/html/body/form/button')
fname.send_keys('aaaaa')
lname.send_keys('bbbbb')
email.send_keys('sldfjlsd@lsadfj.com')
time.sleep(2)
button.click()
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import time, sleep

MY_DATA = '0.1251|922|38|725|21|778|12|1577|4|2929|3|9320|0|50000|0|1000000|0|123456789'
T = 6
driver = webdriver.Edge(edge_driver_path)

driver.get(URL_S[3])

cookie = driver.find_element_by_id('cookie')
print('1')
driver.find_element_by_id('importSave').click()
alter = driver.switch_to.alert
sleep(2)
alter.accept()
sleep(1)
print(2)
# driver.find_element_by_id('importSave').click()
# alter = driver.switch_to.alert
# sleep(2)
# alter.dissmis()
# sleep(1)
print(3)
driver.find_element_by_id('importSave').click()
sleep(2)
Alert(driver).send_keys('helo')
sleep(3)
print(Alert(driver).text)
sleep(5)
driver.close()
# for x in range(size):
#     driver.switch_to.window(handles[x])
#     print(driver.title)
# obj.send_keys(MY_DATA)

# products = driver.find_elements_by_css_selector('#store div')
# for product in products:
#     print(product.text)
# products_id = [itme.get_attribute('id') for itme in products]
#
# time_out = time() + T
# five_min = time() + (60 * 20)

# while True:
#
#     cookie.click()
#     # every 5 second
#     if time() > time_out:
#         prices = driver.find_elements_by_css_selector('#store b')
#         prices = prices[:-1]
#         prices = [int(str(price.text).split('-')[1].replace(',', '')) for price in prices]
#
#         products_dic =  dict(zip(prices, products_id))
#
#         money_element = driver.find_element_by_id('money').text
#         if ',' in money_element:
#             money_element = int(str(money_element).replace(',', ''))
#         else:
#             money_element = int(money_element)
#
#         products_can_bay = {}
#         for cost, id_product in products_dic.items():
#             if cost < money_element:
#                 products_can_bay[cost] = id_product
#         highest_price_can_bay = max(products_can_bay)
#         driver.find_element_by_id(products_can_bay[highest_price_can_bay]).click()
#         time_out = time()+T
#     if time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#
#         break
# driver.close()
