import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def download_images(keyword, num_images, folder_path):
    # Create the subfolder if it does not exist
    subfolder_path = os.path.join(folder_path,"Images of " + keyword)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Configure Chrome webdriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set path to chromedriver in your system
    chrome_driver_path = "E:\Web Crawling\chromedriver.exe"
    service = Service(chrome_driver_path)

    # Start the ChromeDriver service
    service.start()

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Google Images in Chrome
    driver.get("https://www.google.com/imghp")

    # Find the search box and enter the keyword
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)

    # Scroll down to load more images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the page source and parse it using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all image elements
    image_elements = soup.select("img.rg_i")

    # Download the images
    downloaded_images = 0
    for i, image in enumerate(image_elements):
        image_url = image.get("src")

        # Make sure the URL is valid
        if image_url and image_url.startswith("http"):
            try:
                response = requests.get(image_url)
                response.raise_for_status()

                # Save the image to the subfolder
                with open(os.path.join(subfolder_path, f"scraped_{downloaded_images+1}.jpg"), "wb") as file:
                    file.write(response.content)

                downloaded_images += 1

                if downloaded_images >= num_images:
                    break

            except requests.exceptions.RequestException:
                # Handle any errors that occur during image download
                continue

    driver.quit()
    print(f"Downloaded {downloaded_images} images of {keyword}.")

    if downloaded_images < num_images:
        print("Warning: The requested number of images could not be downloaded.")

# Example usage
keyword = input("Enter the search term: ")
num_images = int(input("Enter the number of images to download: "))
folder_path = "E:\Web Crawling\Web scraped"

download_images(keyword, num_images, folder_path)
