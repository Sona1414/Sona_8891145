# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.costco.ca/")
time.sleep(3)


# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","search-field") old syntax
search_bar = driver.find_element("id","search-field")
search_bar.send_keys("table")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "table" in driver.title



# Selecting a table from the search results
table_link = driver.find_element("xpath","//a[@automation-id='productDescriptionLink_0']")
# table_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
table_link.click()





# Waiting for the table details page to load
time.sleep(5)

# Adding the table to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-btn")
add_to_cart_button.click()



time.sleep(5)
# Adding the table to the list
Add_to_list=driver.find_element("xpath","//span[contains(.,'Add to List')]")
Add_to_list.click()


time.sleep(5)
# Sign in page loads
create_account=driver.find_element("xpath","/html/body/div[2]/main/div/div[1]/div[2]/p/a")
create_account.click()

time.sleep(5)

# Closing the webdriver
driver.close()