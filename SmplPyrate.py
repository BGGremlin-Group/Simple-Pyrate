#!/usr/bin/env python3
import os
import sys
import time

# Ensure yt-dlp is installed; exit gracefully if missing.
try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("Error: yt_dlp is not installed. Please install it using 'pip install yt-dlp'")
    sys.exit(1)

# Use colorama for colorful CLI output.
try:
    from colorama import init, Fore, Style
except ImportError:
    # If colorama isn't installed, define dummy color codes.
    class DummyColor:
        RESET_ALL = ''
        RED = ''
        GREEN = ''
        YELLOW = ''
        BLUE = ''
        MAGENTA = ''
        CYAN = ''
        WHITE = ''
    init = lambda: None
    Fore = DummyColor()
    Style = DummyColor()

# Initialize colorama
init(autoreset=True)

# Set a Global Booty Directory (default: "Booty" in the current working directory)
DOWNLOAD_DIR = os.path.join(os.getcwd(), "Booty")
if not os.path.exists(DOWNLOAD_DIR):
    try:
        os.makedirs(DOWNLOAD_DIR)
    except Exception as e:
        print(f"{Fore.RED}Error creating directory for booty: {e}")
        sys.exit(1)
        
def display_banner():
    # A stylish ASCII banner
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}🪐      ☁️                       ☁️
{Fore.WHITE}{Style.BRIGHT}           🏴‍☠️| 🏴‍☠️| 🏴‍☠️|    
{Fore.WHITE}{Style.BRIGHT}             )_)  )_)  )_)    🌛   
{Fore.WHITE}{Style.BRIGHT}            )___))___))___)\            
{Fore.WHITE}{Style.BRIGHT}           )____)____)_____)\\    ☁️
{Fore.YELLOW}         _____|____|____|____\\\__
{Fore.CYAN}{Style.BRIGHT}---------{Fore.YELLOW}\ ° {Fore.GREEN}{Style.BRIGHT}simple 💥 pyrate{Fore.YELLOW} °  /{Fore.CYAN}{Style.BRIGHT}--------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ^^^^  🐬    ^^^^     ^^^    ^^
^^         ^^^^      ^^^     ^       ^^
{Fore.YELLOW}{Style.BRIGHT}=================B=G=G=G==================
"""
    print(banner)
    
def download_video(url, download_dir=DOWNLOAD_DIR, audio_only=False):
    """
    Pirate video (or audio only) from the provided URL using yt-dlp.
    """
    # Define common options.
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': True,  # Single video only; playlists not supported here.
        'quiet': True,       # We'll manage our own logging.
        'no_warnings': True,
    }
    
    if audio_only:
        # Pillage best audio and convert to MP3 using FFmpeg.
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        # Pirate best quality video + audio (fallback to best overall).
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
        })
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # Determine file path based on info.
            title = info.get('title', 'video')
            ext = info.get('ext', 'mp4') if not audio_only else 'mp3'
            file_path = os.path.join(download_dir, f"{title}.{ext}")
            print(f"{Fore.GREEN}Successfully pirated: {title}")
            return file_path
    except Exception as e:
        print(f"{Fore.RED}Error pirating video: {e}")
        return None

# Pirate Single Video
def option_single_download():
    url = input(f"{Fore.YELLOW}Enter the video URL to plunder: {Style.RESET_ALL}").strip()
    if not url:
        print(f"{Fore.RED}No URL provided. Returning to ship.")
        return
    print(f"{Fore.BLUE}Setting Sail for single video plunder...{Style.RESET_ALL}")
    download_video(url)
    time.sleep(1)

# Batch Pirate
def option_batch_download():
    print(f"{Fore.YELLOW}Enter video URLs to plunder, one per line. Type 'booty confirmed'' when finished:{Style.RESET_ALL}")
    urls = []
    while True:
        line = input().strip()
        if line.lower() == 'booty confirmed':
            break
        if line:
            urls.append(line)
    if not urls:
        print(f"{Fore.RED}No URLs entered. Returning to ship.")
        return
    print(f"{Fore.BLUE}Starting boarding process for {len(urls)} videos...{Style.RESET_ALL}")
    for idx, url in enumerate(urls, start=1):
        print(f"{Fore.MAGENTA}[{idx}/{len(urls)}] Boarded. Now Pirating: {url}{Style.RESET_ALL}")
        download_video(url)
        time.sleep(1)  # Brief pause between downloads

# Pirate Audio Only 
def option_audio_only_download():
    url = input(f"{Fore.YELLOW}Enter the video URL for audio plunder extraction: {Style.RESET_ALL}").strip()
    if not url:
        print(f"{Fore.RED}No URL provided. Returning to ship.")
        return
    print(f"{Fore.BLUE}Starting audio-only pirating...{Style.RESET_ALL}")
    download_video(url, audio_only=True)
    time.sleep(1)

# Pirate a full channel
def download_channel(url, download_dir=DOWNLOAD_DIR, audio_only=False):
    """
    Pirate all videos from the provided channel URL using yt-dlp.
    This function overrides the 'noplaylist' option to pillaige the entire channel.
    """
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Allow playlist (channel) downloads.
        'quiet': True,
        'no_warnings': True,
    }
    
    if audio_only:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
        })
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            # This downloads the entire channel playlist
            info = ydl.extract_info(url, download=True)
            print(f"{Fore.GREEN}Successfully Plundered Entire Channel: {url}")
            return info
    except Exception as e:
        print(f"{Fore.RED}Error Pirating Channel: {e}")
        return None

def option_channel_download():
    url = input(f"{Fore.YELLOW}Enter the channel URL to plunder (YouTube/Rumble): {Style.RESET_ALL}").strip()
    if not url:
        print(f"{Fore.RED}No URL provided. Returning to ship.")
        return
    print(f"{Fore.BLUE}Pillaiging channel...{Style.RESET_ALL}")
    download_channel(url)
    time.sleep(1)

def option_channel_audio_only_download():
    url = input(f"{Fore.YELLOW}Enter the channel URL for audio plundering {Style.RESET_ALL}").strip()
    if not url:
        print(f"{Fore.RED}No URL provided. Returning to ship.")
        return
    print(f"{Fore.BLUE}Starting audio-only channel plundering...{Style.RESET_ALL}")
    download_channel(url, audio_only=True)
    time.sleep(1)


#Change Download Dir
def option_change_directory():
    global DOWNLOAD_DIR
    new_dir = input(f"{Fore.YELLOW}Enter new directory path to store ye booty {Style.RESET_ALL}").strip()
    if not new_dir:
        print(f"{Fore.RED}No directory entered. Returning to ship")
        return
    if not os.path.exists(new_dir):
        try:
            os.makedirs(new_dir)
            print(f"{Fore.GREEN}Directory created: {new_dir}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error creating directory: {e}{Style.RESET_ALL}")
            return
    DOWNLOAD_DIR = new_dir
    print(f"{Fore.GREEN}Download directory for the Booty updated to: {DOWNLOAD_DIR}{Style.RESET_ALL}")

def option_exit():
    print(f"{Fore.CYAN}Exiting simple pirate. May the wind be at your back, Captain.{Style.RESET_ALL}")
    sys.exit(0)
    
def main_menu():
    while True:
        print(f"""
{Fore.YELLOW}{Style.BRIGHT}==========================================
         🏴‍☠️☠️Simple•Pyrate☠️🏴‍☠️ !
==========================================
{Fore.GREEN}{Style.BRIGHT}1. Pirate a Single Video
2. Batch Pirate Videos
3. Pirate Audio Only (MP3)
4. Change Booty Directory (Current: {DOWNLOAD_DIR})
5. Pillaige All Videos from a Channel
6. Pillaige Channel's Audio Only
7. Exit
{Style.RESET_ALL}
""")
        choice = input(f"{Fore.MAGENTA}Select an option (1-7): {Style.RESET_ALL}").strip()
        if choice == '1':
            option_single_download()
        elif choice == '2':
            option_batch_download()
        elif choice == '3':
            option_audio_only_download()
        elif choice == '4':
            option_change_directory()
        elif choice == '5':
            option_channel_download()
        elif choice == '6':
            option_channel_audio_only_download()
        elif choice == '7':
            option_exit()
        else:
            print(f"{Fore.RED}Invalid option. Please select a number between 1 and 7.{Style.RESET_ALL}")
        time.sleep(1)
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    main_menu()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Voyage interrupted by the Captain! Abandoning Ship...{Style.RESET_ALL}")
        sys.exit(0)
