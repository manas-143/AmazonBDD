# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Set up Selenium webdriver (make sure you have the appropriate driver installed and its path set)
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver,10)
#
# # Navigate to Amazon.in
# driver.get("https://www.amazon.in/")
#
# # Find the search box and enter the laptop keyword
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# search_box.send_keys("hp laptops")
#
#
# # Click the search button
# search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
# search_button.click()
# parent_url=driver.current_window_handle
#
# # Wait for the search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a.a-link-normal")))
#
# # Find the first three laptops and add them to the cart
# laptop_links = driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
#
# for i in range(len(laptop_links)):
#     laptop_links[i].click()
#     time.sleep(1)
#     web_link=driver.window_handles
# for j in web_link:
#     if j != parent_url:
#         driver.switch_to.window(j)
#         wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button"]'))).click()
#         time.sleep(5)
#         driver.switch_to.window(parent_url)
#
# driver.find_element(By.XPATH,'//div[@id="nav-cart-count-container"]').click()
# time.sleep(2)
# price = driver.find_element(By.XPATH,'//span[@id="sc-subtotal-amount-activecart"]')
# time.sleep(3)
# print(price.text)
#
#
# driver.quit()
