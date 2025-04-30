from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

#----------------------Scrapping the price, location and the links for the results------------------------------


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.getText().strip("+/mo")  for price in prices]
price_list = [item.strip("+ 1bd") for item in price_list]

addresses = soup.find_all("address")
locations = [address.text.replace("|", "").replace("#", " ").strip() for address in addresses]

links = soup.find_all("a", class_="property-card-link")
link_list = [link["href"] for link in links]


# -----------------------Using selenium for the automation of form filling--------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScD3fZgCrAJc1ygPlh0mvdJ0-3k9zKVguSvadSI0VQOaITB8g/viewform?usp=header")

for i in range(len(addresses)):
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address_input.click()
    address_input.send_keys(locations[i], Keys.ENTER)

    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(price_list[i], Keys.ENTER)

    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    link_input.click()
    link_input.send_keys(link_list[i], Keys.ENTER)

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    submit.click()

    new_re = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    new_re.click()