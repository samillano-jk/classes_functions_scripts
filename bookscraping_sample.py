from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup

options = ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
url = "https://quotes.toscrape.com/"

driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")

for box in soup.find_all("div", "quote"):
    author = box.find("small", "author").text
    quote = box.find("span", "text").text
    tag = box.find("div", "tags").text.replace("Tags:", "").strip()
    print(f"Author: {author}")
    print(f"{quote}")
    print(f"Tags:{tag}")
    print()

driver.quit()

