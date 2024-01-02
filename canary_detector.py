import os
import zipfile
import re
import shutil
import time


PATH_TO_CHECK = '0sdk127so0set1nt5vxp1gc90.docx'

RED = '\033[91m'
RESET = '\033[0m'


def decompress_and_scan(file_path):
    suspicious = False  # Flag to track if suspicious URLs are found
    temp_dir = "temp_extracted"
    os.makedirs(temp_dir, exist_ok=True)
    original_path = file_path  # Store the original file path
    new_path = file_path + ".zip"  # Define the new file path

    try:
        if os.path.exists(file_path):
            os.rename(file_path, new_path)
            with zipfile.ZipFile(new_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            url_pattern = re.compile(r'https?://\S+')
            ignored_domains = ['schemas.openxmlformats.org', 'schemas.microsoft.com', 'purl.org','w3.org']

            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', errors='ignore') as file:
                        contents = file.read()
                        urls = url_pattern.findall(contents)
                        for url in urls:
                            if not any(domain in url for domain in ignored_domains):
                                print(f"URL Found: {url}")
                                suspicious = True  # Mark as suspicious if a non-ignored URL is found

    except Exception as e:
        print(f"Error processing file {original_path}: {e}")

    finally:
        shutil.rmtree(temp_dir)
        try:
            if os.path.exists(new_path):
                os.rename(new_path, original_path)
        except Exception as e:
            print(f"Error cleaning up: {e}")

    return suspicious

def is_suspicious(file_path):
    if file_path.endswith(('.docx', '.xlsx', '.pptx')):
        return decompress_and_scan(file_path)

    return False

def main():
    if os.path.isfile(PATH_TO_CHECK):
        if is_suspicious(PATH_TO_CHECK):
            print(RED + f"The file {PATH_TO_CHECK} is suspicious." + RESET)
        else:
            print(f"The file {PATH_TO_CHECK} seems normal.")
    elif os.path.isdir(PATH_TO_CHECK):
        for root, dirs, files in os.walk(PATH_TO_CHECK):
            for name in files:
                file_path = os.path.join(root, name)
                if is_suspicious(file_path):
                    print(RED + f"The file {file_path} is suspicious." + RESET)
                else:
                    print(f"The file {file_path} seems normal.")

if __name__ == "__main__":
    main()
