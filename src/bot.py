from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json
import time
from config import ProductDetails, UserDetails, PaymentDetails, ChromeOptions

headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                         'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                 "Version/13.0.3 Mobile/15E148 Safari/604.1"}

prefs = {'disk-cache-size': 4096}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options, executable_path=ChromeOptions.CHROME_DRIVER_PATH)
wait = WebDriverWait(driver, 10)
session = requests.Session()


def find_item_id(name):
    """
    Find Item on Supreme web-store and return its unique item ID
    """

    url = 'https://www.supremenewyork.com/mobile_stock.json'

    html = session.get(url=url, headers=headers, timeout=10)
    output = json.loads(html.text)

    for category in output['products_and_categories']:
        for item in output['products_and_categories'][category]:
            if name in item['name']:
                print(item['name'])
                print(item['id'])
                return item['id']


def find_item(product_id, colour, size):
    """
    Finds and returns the unique colour ID for the chosen item
    """

    url = 'https://www.supremenewyork.com/shop/' + str(product_id) + '.json'

    html = session.get(url=url, headers=headers, timeout=10)
    output = json.loads(html.text)

    for product_colours in output['styles']:
        if colour in product_colours['name']:
            for product_size in product_colours['sizes']:
                if size in product_size['name']:
                    return product_colours['id']


def get_product(product_id, product_colour_id, size):
    """
    Opens Chrome instance and adds product to card
    """

    url = 'https://www.supremenewyork.com/mobile/#products/' + str(product_id) + '/' + str(product_colour_id)

    driver.get(url)

    wait.until(EC.presence_of_element_located((By.ID, 'size-options')))

    options = Select(driver.find_element_by_id('size-options'))
    options.select_by_visible_text(size)

    driver.find_element_by_xpath("//*[@id='cart-update']/span").click()


def checkout():
    """
    Inputs checkout details
    """
    driver.get('https://www.supremenewyork.com/mobile/#checkout')

    wait.until(EC.presence_of_element_located((By.ID, 'order_billing_name')))
    driver.execute_script(
        f'document.getElementById("order_billing_name").value="{UserDetails.NAME}";'
        f'document.getElementById("order_email").value="{UserDetails.EMAIL}";'
        f'document.getElementById("order_tel").value="{UserDetails.TELE}";'
        f'document.getElementById("order_billing_address").value="{UserDetails.ADDRESS_1}";'
        f'document.getElementById("order_billing_address_2").value="{UserDetails.ADDRESS_2}";'
        f'document.getElementById("order_billing_address_3").value="{UserDetails.ADDRESS_3}";'
        f'document.getElementById("order_billing_city").value="{UserDetails.CITY}";'
        f'document.getElementById("order_billing_zip").value="{UserDetails.POSTCODE}";'
        f'document.getElementById("credit_card_number").value="{PaymentDetails.CARD_NUMBER}";'
        f'document.getElementById("credit_card_cvv").value="{PaymentDetails.CVV}";'
    )

    card_month = Select(driver.find_element_by_id('credit_card_month'))
    card_month.select_by_value(str(PaymentDetails.EXP_MONTH))

    card_year = Select(driver.find_element_by_id('credit_card_year'))
    card_year.select_by_value(str(PaymentDetails.EXP_YEAR))

    driver.find_element_by_id('order_terms').click()

    driver.find_element_by_id('submit_button').click()


if __name__ == '__main__':
    t1 = time.time()
    product_id = find_item_id(ProductDetails.KEYWORDS)
    product_colour_id = find_item(product_id, ProductDetails.COLOUR, ProductDetails.SIZE)
    get_product(product_id, product_colour_id, ProductDetails.SIZE)
    time.sleep(0.5)
    checkout()
    t0 = time.time()
    print('TIME: ', t0 - t1)
