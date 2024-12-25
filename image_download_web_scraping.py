import os
import requests
from bs4 import BeautifulSoup

# Function to create a folder for storing images
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to download images for a given query
def download_images(query, folder_name, num_images=30):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    count = 0
    page = 0

    while count < num_images:
        search_url = f"https://www.google.com/search?q={query}&tbm=isch&start={page * 20}"
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch the webpage for {query}.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img")

        if not images:
            print(f"No more images found for {query}.")
            break

        for i, img_tag in enumerate(images):
            if count >= num_images:
                break

            try:
                img_url = img_tag.get("src")
                if not img_url or not img_url.startswith("http"):
                    continue

                img_data = requests.get(img_url).content
                file_path = os.path.join(folder_name, f"{folder_name}_{count + 1}.jpg")

                with open(file_path, "wb") as img_file:
                    img_file.write(img_data)

                count += 1
                print(f"Downloaded {file_path}")
            except Exception as e:
                print(f"Failed to download image {count + 1} for {query}: {e}")

        page += 1  # Increment to the next page of results

# Main execution
if __name__ == "__main__":
    players = [
        "Lionel Messi",
        "Virat Kohli",
        "Maria Sharapova",
        "Usain Bolt",
        "Saina Nehwal"
    ]
    images_count = 30

    for player in players:
        folder_name = player.lower().replace(" ", "_")
        create_folder(folder_name)
        download_images(player.replace(" ", "+"), folder_name, images_count)