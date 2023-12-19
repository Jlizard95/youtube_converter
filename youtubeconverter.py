import os
import pytube

def download_video():
    url = input("Enter the URL of the YouTube video: ")
    yt = pytube.YouTube(url)
    print("Select the file format:")
    print("1. MP4")
    print("2. MP3")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        folder = 'Video'
        extension = '.mp4'
    elif choice == 2:
        stream = yt.streams.filter(only_audio=True).first()
        folder = 'Music'
        extension = '.mp3'
    else:
        print("Invalid choice.")
        return
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = stream.default_filename[:-4] + extension
    stream.download(output_path=folder, filename=filename)
    print(f"Download complete. The file is saved in the '{folder}' folder as '{filename}'.")
    
download_video()