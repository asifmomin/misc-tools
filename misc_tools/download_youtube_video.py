import argparse
from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=path)
    print(f"Downloaded '{yt.title}' to '{path}' successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a YouTube video to a local directory.")
    parser.add_argument("url", help="The URL of the YouTube video you wish to download.")
    parser.add_argument("path", help="The local path where you want to save the downloaded video.")
    
    args = parser.parse_args()

    download_video(args.url, args.path)
