import os
from bs4 import BeautifulSoup

def extract_urls_from_xml(xml_folder, output_file):
    """
    Extracts URLs from <loc> tags in XML files and saves them to a text file.
    
    :param xml_folder: The folder containing XML files.
    :param output_file: The text file to save the extracted URLs.
    """
    urls = []
    
    # Loop through each XML file in the specified folder
    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_file)
            try:
                # Open and parse the XML file with BeautifulSoup
                with open(xml_path, 'r') as file:
                    soup = BeautifulSoup(file, 'xml')
                
                # Find all <loc> tags and extract the URLs
                for loc in soup.find_all('loc'):
                    url: str = loc.text.strip()
                    if url:
                        urls.append(url)
            except Exception as e:
                print(f"Failed to parse {xml_file}: {e}")
    
    # Save the extracted URLs to the output file
    with open(output_file, 'w') as file:
        for url in urls:
            file.write(url + '\n')
    
    print(f"Extracted {len(urls)} URLs to {output_file}")

# 

if __name__ == "__main__":
    # Define paths
    xml_folder = '1@_sitemaps'  # Folder containing the XML files
    output_file = '2@_compressed_sitemaps.txt'  # Text file to save the extracted URLs
    
    # Extract URLs and save to a file
    extract_urls_from_xml(xml_folder, output_file)