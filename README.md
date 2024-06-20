### Updated Documentation with Troubleshooting Steps

### Overview

This Python script automates the process of crawling and downloading images from Bing based on user-defined search keywords. It uses libraries like Selenium for web navigation, PIL for image processing, and pandas for data management. Command-line parameters are supported through argparse, offering flexibility for different search queries.

### Requirements

- Python 3.x
- Selenium
- pandas
- Pillow (PIL Fork)
- tqdm
- urllib

Ensure that you have the Chrome WebDriver installed and properly set up in your system's PATH.

### Installation

1. Install the necessary Python packages:
   ```bash
   pip install selenium pandas Pillow tqdm urllib3
   ```

2. Download and install the Chrome WebDriver. Make sure it matches the version of Chrome you have installed on your system. You can download it from [Chrome WebDriver](https://sites.google.com/chromium.org/driver/home).

### Running the Script

Execute the script from the command line with the search keyword as an argument:
```bash
python crawler_argparse.py "Birds"
```
Replace `"Birds"` with the search keyword of your choice.

### Script Workflow

![WindowsTerminalDemo](WindowsTerminalDemo.gif)


1. **Initialization**: Parses command-line arguments for search keywords and sets up directories for storing images and links.
2. **Selenium WebDriver Setup**: Initializes Chrome WebDriver to interact with Bing's image search.
3. **Search and Navigation**: Navigates to Bing Images, inputs the search terms, and tweaks the URL for specific image traits.
4. **Scrolling and Interaction**: Simulates page scrolling and clicks "see more" buttons to load additional images.
5. **Image Crawling and Downloading**:
   - Extracts URLs from image thumbnails.
   - Downloads images to the specified directories.
6. **Link Storage**: Saves the collected image URLs into a CSV file in a separate directory.
7. **Cleanup**: Includes a significant delay for demonstration purposes before closing the browser.

### Troubleshooting

#### Common Issues

If you encounter the following error:

```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 111
```

This indicates a version mismatch between ChromeDriver and your installed version of Chrome.

#### Solution

1. Identify your Chrome version by navigating to `chrome://settings/help` in your Chrome browser.
2. Visit the following links to find and download the ChromeDriver that corresponds to your version of Chrome:
   - [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/home)
   - [ChromeDriver - Downloads](https://sites.google.com/chromium.org/driver/downloads)
If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. 
   - [ChromeDriver - Downloads 115 or newer](https://googlechromelabs.github.io/chrome-for-testing/)
This page provides convenient JSON endpoints for specific ChromeDriver version downloading.
3. Replace the existing `chromedriver.exe` in your project folder with the downloaded version.

### Notes

- **Error Handling**: Basic error handling is included, but you might need enhanced mechanisms for specific use cases.
- **Execution Time**: Delays (`time.sleep`) are integrated to simulate human-like interactions; adjust these based on your needs.
- **Storage Requirements**: Ensure ample storage for downloaded images and manage directories appropriately for multiple search sessions.

