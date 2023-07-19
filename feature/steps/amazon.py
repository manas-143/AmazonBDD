import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''-----------all the locators-------------'''
Locators={"search_box":"twotabsearchtextbox",

          "search_button": "//input[@value='Go']",

          "rating_review_span_class":"span.a-icon-alt",

          "laptop_list_div" : '//div[@data-component-type="s-search-result"]',

          "add_to_cart_button" :'//input[@id="add-to-cart-button"]',

          "Price_tag" : '//span[@class="a-price-whole"][1]',

          "cart_icon" : '//div[@id="nav-cart-count-container"]',

          "total_price" : '//span[@id="sc-subtotal-amount-activecart"]'
          }
'''---------------------------------------------------------------------------------------'''

@given("the Customer is on the Amazon.in homepage")
def amazon_login(context):
    context.driver = webdriver.Chrome()
    context.wait = WebDriverWait(context.driver, 15)
    context.driver.get("https://www.amazon.in/") #amazon webpage


@when('the Customer searches for "{search_query}"')
def search_for_laptops(context, search_query):
    search_box = context.driver.find_element(By.ID,Locators["search_box"] )
    search_box.send_keys(search_query) #------------------------------------contains search items
    search_button = context.driver.find_element(By.XPATH,Locators["search_button"])
    search_button.click()
    context.parent_url = context.driver.current_window_handle
    context.amount = []#---------------------------------------------empty list to add the amount
    context.laptops_to_add = []#-------------------------------------empty list to add the highest rated items

@then("the Customer adds three highly-rated Dell laptops to the cart")
def add_laptops_to_cart(context):
    laptop_links = context.driver.find_elements(By.XPATH, Locators["laptop_list_div"])
    for laptop_element in laptop_links:
        rating_elements = laptop_element.find_elements(By.CSS_SELECTOR,Locators["rating_review_span_class"] )
        rating = rating_elements[0].get_attribute("innerHTML").split()[0] if rating_elements else "N/A" #to get the texts in the links
        if rating >= "4.0":
            context.laptops_to_add.append(laptop_element)

            '''to add the highest rated laptops'''
    laptops_added = 0
    for laptop_link in context.laptops_to_add:
        laptop_link.click()
        time.sleep(2)
        web_link = context.driver.window_handles #------------------contains parent web link
        '''--------------------------------------'''
    for item in web_link:
        if item != context.parent_url:
            context.driver.switch_to.window(item)
            wait = WebDriverWait(context.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, Locators["add_to_cart_button"])))
            price_element = context.driver.find_element(By.XPATH,Locators["Price_tag"] ) #----------price webelement of laptop
            p = price_element.get_attribute("innerHTML")#price of laptop
            context.amount.append(p.replace('<span class="a-price-decimal">.</span>', ""))
            add_to_cart = context.driver.find_element(By.XPATH, Locators["add_to_cart_button"])
            add_to_cart.click()

            time.sleep(5)
            context.driver.switch_to.window(context.parent_url)
            laptops_added += 1
            if laptops_added == 3:
                break

@then("the Customer verifies the total price in the cart")
def price_compare(context):
    cart_button = context.driver.find_element(By.XPATH,Locators["cart_icon"] )
    cart_button.click()
    time.sleep(2)

    price = context.driver.find_element(By.XPATH, Locators["total_price"])
    time.sleep(3)
    final_price = price.text
    final_price = float(final_price.replace(",", ""))

    total_amount = sum(float(x.replace(',', '')) for x in context.amount)

    assert final_price == total_amount, "Total price in cart does not match with expected."

@then('the Customer closes the browser')
def close_browser(context):
    context.driver.quit()
