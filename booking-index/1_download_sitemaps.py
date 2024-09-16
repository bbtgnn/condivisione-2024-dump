import requests
import os

def download_urls(file_path, download_folder):
    # Check if the download folder exists, if not, create it
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Read the file containing the URLs
    with open(file_path, 'r') as file:
        urls = file.readlines()

    # Download each URL
    for i, url in enumerate(urls):
        url = url.strip()
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful
                
                # Generate a file name based on the URL
                file_name = url.split("/")[-1]
                
                # Save the content to the file
                with open(os.path.join(download_folder, file_name), 'wb') as output_file:
                    output_file.write(response.content)
                
                print(f"Downloaded: {url}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    file_path = '0_sitemaps.txt'  # Path to the file containing the URLs
    download_folder = '1@_sitemaps'  # Folder to save the downloaded files

    download_urls(file_path, download_folder)
