# Python
import os
import time
import glob

def is_file_downloaded(expected_file_name, file_extension, timeout):
    folder_name = os.getenv('DOWNLOAD_FOLDER_PATH')
    print(f"Download Folder Path: {folder_name}")
    print("Make sure the folder path is correct!")

    file_downloaded = False
    start_time = time.time()
    wait_time = start_time + timeout

    while time.time() < wait_time:
        list_of_files = glob.glob(os.path.join(folder_name, f'*{file_extension}'))

        for file in list_of_files:
            file_name = os.path.basename(file)

            if not "crdownload" in file_name and expected_file_name in file_name:
                print(f"Name of the found file: {file_name}")
                file_downloaded = True
                os.remove(file)
                break

        if file_downloaded:
            break

    return file_downloaded