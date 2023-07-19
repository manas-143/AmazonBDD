# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Set up Selenium webdriver (make sure you have the appropriate driver installed and its path set)
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 15)
#
# # Navigate to Amazon.in
# driver.get("https://www.amazon.in/")
#
# # Find the search box and enter the laptop keyword
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# search_box.send_keys("dell laptops")
#
# # Click the search button
# search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
# search_button.click()
# parent_url = driver.current_window_handle
#
# # Wait for the search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a.a-link-normal")))
#
# # Find the laptop links
# laptop_links = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
# amount=[]
# l=[]
# for laptop_element in laptop_links:
#     rating_elements = laptop_element.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
#     rating = rating_elements[0].get_attribute("innerHTML").split()[0] if rating_elements else "N/A"
#     if rating >="4.0":
#         l.append(laptop_element)
#
# # Counter variable to track the number of laptops added
# laptops_added = 0
#
#
# # Loop through the laptop links
# for laptop_link in l:
#     laptop_link.click()
#     time.sleep(2)
#     web_link = driver.window_handles
#
#
#
#
# for j in web_link:
#     if j != parent_url:
#
#         driver.switch_to.window(j)
#         wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button"]')))
#         price_element = driver.find_element(By.XPATH, '//span[@class="a-price-whole"][1]')
#         p = price_element.get_attribute("innerHTML")
#         amount.append(p.replace('<span class="a-price-decimal">.</span>',""))
#         driver.find_element(By.XPATH,'//input[@id="add-to-cart-button"]').click()
#         time.sleep(5)
#         driver.switch_to.window(parent_url)
#
#         laptops_added += 1
#         if laptops_added == 3:
#             break
#
#
#
# # Go to the cart
# driver.find_element(By.XPATH, '//div[@id="nav-cart-count-container"]').click()
# time.sleep(2)
#
# # Get the subtotal price
# price = driver.find_element(By.XPATH, '//span[@id="sc-subtotal-amount-activecart"]')
# time.sleep(3)
# final_price=price.text
# final_price=float(final_price.replace(",",""))
# print(price.text)
# print((amount))
# total_amount = sum(float(x.replace(',', '')) for x in amount)
# if final_price == total_amount:
#     print("matched")
#
# driver.quit()
