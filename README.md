## Web Scraper for Images
This code is designed to download images from the internet using a specified keyword and save them to a designated folder.
## Features
- Downloads a specified number of images related to a given keyword from any server.
- Uses Selenium for browser automation and BeautifulSoup for parsing HTML content.
## Installation

- Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WebScraper.git
   cd WebScraper
- **Create a Virtual Environment**:
  ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- **Install Dependencies**:
  ```sh
  pip install -r requirements.txt
##Usage

- 
2. **Adjust Path Variables:**
   - Modify `folder_path` in the script to specify where you want to save the downloaded images.
   - Update `chrome_driver_path` to point to the location of `chromedriver.exe` on your system.

   Example:
   ```python
   # Set path to chromedriver in your system
   chrome_driver_path = "path/to/your/chromedriver.exe"
   
   # Specify the folder path where images will be saved
   folder_path = "path/to/your/download/folder"
- Run the application with the following command:
  ```sh
  python WebScraper.py
- Enter the search term (keyword) when prompted.
- Enter the number of images to download.
- Images will be saved in the Images of [keyword] folder under the specified folder_path.

## Dependencies

 - **os**: Provides functions for interacting with the operating system, such as creating directories and handling file paths.
 - **time**: Offers time-related functions, used for adding delays during the scrolling process.
 - **requests**: Enables sending HTTP requests to retrieve image data.
 - **BeautifulSoup (from bs4 package)**: A library for parsing HTML and XML documents. Here, it's used to parse the page source of Google Images.
 - **selenium**: A web testing framework that allows automation of web browsers. It's used here to control the Chrome browser and interact with Google Images.
 - **[Chrome WebDriver](https://sites.google.com/chromium.org/driver/downloads)**(`chromedriver.exe` for Windows, or `chromedriver` for macOS/Linux) must be installed and configured in the system PATH.
## How it works?

- Creates a subfolder within the specified folder path to store the images.
- Configures the Chrome webdriver options to run Chrome in headless mode (without a visible browser window).
- Sets the path to the Chrome webdriver (chromedriver.exe) on your system.
- Starts the ChromeDriver service.
- Creates a new instance of the Chrome driver.
- Finds the search box of the search engine and enters the specified keyword.
- Search for the images
- Scrolls down the page to load more images.
- Retrieves the page source and parses it using BeautifulSoup.
- Finds all the image elements using the CSS selector "img.rg_i".
- Downloads the images one by one by sending HTTP requests to their source URLs, using the requests library.
- Saves each downloaded image to the subfolder with a unique name.
- Quits the Chrome driver.
- Prints the number of images downloaded.
- Displays a warning if the requested number of images could not be downloaded.
- The user will be asked for the keyword and then the number of images to be downloaded, and then the images will be saved in the folder you asked.

