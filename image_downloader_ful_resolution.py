import requests, lxml, re, json, urllib.request
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
}

params = {
    "q": "patty page naked", # search query
    "tbm": "isch",                # image results
    "hl": "en",                   # language of the search
    "gl": "us",                   # country where search comes from
    "ijn": "0"                    # page number
}

html = requests.get("https://www.google.com/search", params=params, headers=headers)

soup = BeautifulSoup(html.text, "lxml")
def get_original_images():

    num_images=int(input("enter the number of images you want to download:\n"))

    all_script_tags = soup.select("script")
    matched_images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

    matched_images_data_fix = json.dumps(matched_images_data)
    matched_images_data_json = json.loads(matched_images_data_fix)

    # https://regex101.com/r/VPz7f2/1
    matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', matched_images_data_json)
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data))

    matched_google_full_resolution_images = re.findall(r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails)
    full_res_images = [
        bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape") for img in matched_google_full_resolution_images
    ]
    # print(full_res_images)
    count = 0
    for original in full_res_images:
        print(count)
        if count == num_images:
            break
        try:
            print(original)
            img_response = requests.get(original)
            with open("F:/download/"+ params["q"]+ "_" + str(count+1) + ".jpg", "wb") as f:
                f.write(img_response.content)
            count += 1
        except:
            pass

    print("Downloaded" + str(num_images)+ " images for "+ params["q"])

get_original_images()