import os

download_path = r'C:\Users\owner\Downloads'

files_in_download = os.listdir(download_path)

folders = []

for file in files_in_download:
    split_name = os.path.splitext(file)
    extension = split_name[1].replace(".", "")
    match extension:
        case "zip":
            file_name = "Zip Files"
        case "exe":
            file_name = "Applications"
        case "jar":
            file_name = "Java Files"
        case "jpg":
            file_name = "Pictures"
        case "m4a":
            file_name = "Music"
        case "mp3":
            file_name = "Music"
        case "msi":
            file_name = "Applications"
        case "pdf":
            file_name = "Documents"
        case "ppt":
            file_name = "Documents"
        case "txt":
            file_name = "Documents"
        case "mp4":
            file_name = "Videos"
        case _:
            file_name = "Others"

    if split_name[1] == "":
        folders.append(file)
    else:
        if os.path.exists(f"{download_path}\\{file_name}"):
            os.replace(f"{download_path}\\{file}",f"{download_path}\\{file_name}\\{file}")

        else:
            os.mkdir(f"{download_path}\\{file_name}")
            os.replace(f"{download_path}\\{file}", f"{download_path}\\{file_name}\\{file}")



