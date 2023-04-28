from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from urllib.request import Request, urlopen

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://pixabay.com/images/search/물고기/"
driver.get(url = url)

image_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]/div[9]/div/div/div/a/img"
image_url = driver.find_element(By.XPATH, image_xpath).get_attribute('src')
print("image_url:", image_url)

image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
f = open("fish.jpg", "wb")
f.write(urlopen(image_byte).read())
f.close()

#sleep(15)