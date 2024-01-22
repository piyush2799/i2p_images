import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_images(url, folder):
    """Downloads all images from a given URL and saves them to the specified folder.

    Args:
        url (str): The URL of the webpage containing the images.
        folder (str): The path to the folder where the images will be saved.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }  # Chrome user-agent

    try:
        os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist

        response = requests.get(url, headers=headers)  # Add headers to the request
        response.raise_for_status()  # Raise an exception for error status codes


        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')

        for image in images:
            image_url = image.get('src')
            if image_url and image_url.startswith('http'):  # Check for valid image URLs
                filename = os.path.basename(image_url)  # Extract filename from URL
                filepath = os.path.join(folder, filename)

                try:
                    image_response = requests.get(image_url, stream=True)
                    image_response.raise_for_status()  # Raise an exception for error status codes

                    with open(filepath, 'wb') as f:
                        for chunk in image_response.iter_content(1024):
                            f.write(chunk)

                    print(f"Image saved: {filename}")
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {image_url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")



df=pd.read_csv("i2p_benchmark.csv" )
path_to_dataset = "i2p_images/"

for i,k in enumerate(df["lexica_url"]):
    download_folder=os.path.join(path_to_dataset,"prompt_"+str(i))
    print(download_folder)
    url_to_scrape = k
    os.makedirs(download_folder, exist_ok=True)
    download_images(url_to_scrape, download_folder)