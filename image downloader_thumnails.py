import requests
# from requests import get
from bs4 import BeautifulSoup
import os

# Set the search query and number of images to download
query = "house hd"
num_images = 2

# Define the Google Images URL
url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"

# Send an HTTP request to the URL and get the response
response = requests.get(url).text

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response, 'html.parser')
# print(soup)
# Find all the img tags with class 'rg_i'
img_tags = soup.find_all("img")
# img_tags=soup.find('div',class_=" bRMDJf islir")
# print(img_tags)
# Create a directory to save the images
# if not os.path.exists(query):
#     os.mkdir(query)

# for img in img_tags:
#     link=img.get("src")
#     print(link)
# Download the images
count = 0
for img_tag in img_tags:
    if count == num_images:
        break
    try:
        # Get the image URL
        # if 'https://encrypted' in img_tag['src']:
        #     pass
        # elif 'http' in img_tag['src']:
        #     img_url = img_tag['src']
        # else:
        #     pass
    
        img_url = img_tag['src']
        print(img_url)
        # Send an HTTP request to the image URL and get the response
        img_response = requests.get(img_url)

        # Save the image to the directory
        with open("F:/download/"+query + "_" + str(count+1) + ".jpg", "wb") as f:
            f.write(img_response.content)
        count += 1
    except:
        pass

print(f"Downloaded {count} images for {query}")
