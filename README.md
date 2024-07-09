## Web Scraper for Images
This code is designed to download images from the internet using a specified keyword and save them to a designated folder.

Here's a breakdown of what the code does and the modules and functions it utilizes:
Modules:

 os: Provides functions for interacting with the operating system, such as 
 creating directories and handling file paths.
 time: Offers time-related functions, used for adding delays during the scrolling process.
 requests: Enables sending HTTP requests to retrieve image data.
 BeautifulSoup (from bs4 package): A library for parsing HTML and XML documents. Here, it's used to parse the page source of Google Images.
 selenium: A web testing framework that allows automation of web browsers. It's used here to control the Chrome browser and interact with Google Images.
Functions:

    download_images(keyword, num_images, folder_path): This function is responsible for the main image downloading process. It takes three parameters:
        keyword: The search term for images.
        num_images: The number of images to download.
        folder_path: The path to the folder where the images will be saved.
    The function performs the following steps:
        Creates a subfolder within the specified folder path to store the images.
        Configures the Chrome webdriver options to run Chrome in headless mode (without a visible browser window).
        Sets the path to the Chrome webdriver (chromedriver.exe) on your system.
        Starts the ChromeDriver service.
        Creates a new instance of the Chrome driver.
        Finds the search box of the search engine and enters the specified keyword.
	Search for the images
        Scrolls down the page to load more images.
        Retrieves the page source and parses it using BeautifulSoup.
        Finds all the image elements using the CSS selector "img.rg_i".
        Downloads the images one by one by sending HTTP requests to their source URLs, using the requests library.
        Saves each downloaded image to the subfolder with a unique name.
        Quits the Chrome driver.
        Prints the number of images downloaded.
        Displays a warning if the requested number of images could not be downloaded.

The user will be asked for the keyword and then the number of images to be downloaded, and then the images will be saved in the folder you asked.
