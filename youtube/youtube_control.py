from selenium import webdriver
from selenium.webdriver.common.by import By
from config.settings import CHROME_DRIVER_PATH, YOUTUBE_URL

def is_youtube_playing():
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(YOUTUBE_URL)
    try:
        video = driver.find_element(By.TAG_NAME, 'video')
        is_playing = video.get_attribute('paused') == 'false'
        return is_playing
    finally:
        driver.quit()
