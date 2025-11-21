import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Automatically update pytube to latest GitHub version
import subprocess
import sys

try:
    import pytube
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/pytube/pytube"])
    import pytube

# Patch pytube if outdated
try:
    from pytube import YouTube, Playlist
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "git+https://github.com/pytube/pytube"])
    from pytube import YouTube, Playlist

def download_video(url, path='.'):
    try:
        if "playlist" in url or "list=" in url:
            pl = Playlist(url)
            print(f"Downloading playlist: {pl.title} ({len(pl.video_urls)} videos)")
            for vid in pl.videos:
                print("Downloading:", vid.title)
                vid.streams.get_highest_resolution().download(output_path=path)
        else:
            yt = YouTube(url)
            print("Title:", yt.title)
            yt.streams.get_highest_resolution().download(output_path=path)
            print("Download completed!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_path = input("Enter download path (leave empty for current folder): ")
    download_video(video_url, download_path if download_path else '.')
