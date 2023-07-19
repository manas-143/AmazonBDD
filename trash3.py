# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
#
# # Find the search input field and enter "HP laptops" as the search query
# search_input = driver.find_element(By.ID, "twotabsearchtextbox")
# search_input.send_keys("HP laptops")
# search_input.send_keys(Keys.RETURN)
#
# # Wait until the search results page is loaded
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.ID, "search")))
#
# # Find all the laptop elements on the page
# laptop_elements = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
# parent_url=driver.current_window_handle
#
# # Store the laptop information in a list
# laptops = []
# for laptop_element in laptop_elements:
#     title_element = laptop_element.find_element(By.CSS_SELECTOR, ".a-link-normal .a-text-normal")
#     price_element = laptop_element.find_element(By.CSS_SELECTOR, ".a-price-whole")
#     rating_elements = laptop_element.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")
#
#     title = title_element.text
#     price = price_element.text
#     rating = rating_elements[0].get_attribute("innerHTML").split()[0] if rating_elements else "N/A"
#     if rating>"4.0":
#         laptop_info = {
#             "title": title,
#             "price": price,
#             "rating": rating
#         }
#         laptops.append(laptop_info)
#
# # Close the browser
# driver.quit()
#
# # Print the list of HP laptops
# for laptop in laptops:
#     print("Title:", laptop["title"])
#     print("Price:", laptop["price"])
#     print("Rating:", laptop["rating"])
#     print()
