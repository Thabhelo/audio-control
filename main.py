import time
import logging
from spotify.spotify_control import pause_spotify, play_spotify
from youtube.youtube_control import is_youtube_playing
from config.settings import CHECK_INTERVAL

# Configure logging to write to a file named 'app.log'
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        while True:
            try:
                # Assuming 'driver' is initialized elsewhere
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
        driver.quit()  # Assuming 'driver' is initialized elsewhere

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