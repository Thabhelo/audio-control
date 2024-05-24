import time
import logging
from selenium.webdriver.common.by import By
from spotify.spotify_control import pause_spotify, play_spotify
from youtube.youtube_control import is_youtube_playing
from config.settings import CHECK_INTERVAL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Initialize the Chrome WebDriver object
chromedriver_path = '/usr/local/bin/chromedriver' # Path to Chromedriver executable

# Initialize ChromeOptions
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome WebDriver with the path to Chromedriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Configure logging to write to a file named 'app.log'
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        while True:
            try:
                playing = is_youtube_playing(driver)
                if playing:
                    pause_spotify()
                else:
                    play_spotify()
                time.sleep(CHECK_INTERVAL)
            except KeyboardInterrupt:
                logging.info("Script terminated by user.")
                break
            except Exception as e:
                # Log any unexpected errors
                logging.error(f"An unexpected error occurred: {e}")

    finally:
        # Clean up resources
        driver.quit()

def is_youtube_playing(driver):
    try:
        video = driver.find_element(By.TAG_NAME, 'video')
        is_playing = video.get_attribute('paused') == 'false'
        # Log the state of the YouTube video
        logging.info(f"YouTube video is {'playing' if is_playing else 'paused'}")
        return is_playing
    except Exception as e:
        # Log any errors that occur while checking the video state
        logging.error(f"Error checking YouTube video state: {e}")
        return False

if __name__ == "__main__":
    main()