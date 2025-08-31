# 🏴‍☠️ Simple Pirate by the BG Gremlin Group 🏴‍☠️

Welcome to **Simple Pirate**, a swashbuckling Python tool by the **BG Gremlin Group** for plundering videos and audio from YouTube, Rumble, and other titillating wonders ofbthe digital seas
Built with `yt-dlp`, this CLI application offers a user-friendly interface to download single videos, entire channels, or audio-only files with a pirate-themed flair! ☠️

---

## 🚢 Features

| Feature | Description |
|---------|-------------|
| 🖼️ **Single Video Download** | Pirate a single video in the best quality available. |
| 📦 **Batch Download** | Plunder multiple videos by providing a list of URLs. |
| 🎵 **Audio-Only Extraction** | Extract audio as MP3 files with customizable quality. |
| 📺 **Channel Download** | Pillage all videos from a YouTube or Rumble channel. |
| 🎙️ **Channel Audio-Only** | Extract audio from all videos in a channel. |
| 📂 **Customizable Booty Directory** | Set where your plundered treasures are stored. |
| 🌈 **Colorful CLI** | Enhanced with `colorama` for vibrant terminal output. |
| 🐬 **Pirate-Themed Interface** | A fun, pirate-inspired ASCII art and messaging. |

---

## 🛠️ Installation

### Prerequisites
- **Python 3.6+**
- **FFmpeg** (required for audio extraction)
- Install required Python packages:
  ```bash
  pip install yt-dlp colorama
  ```

### Steps
1. Clone or download the script from the repository.
2. Ensure `yt-dlp` and `colorama` are installed.
3. Install **FFmpeg** on your system:
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) or use a package manager like `choco install ffmpeg`.
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg` (Ubuntu/Debian) or equivalent.
4. Run the script:
   ```bash
   python3 simple_pirate.py
   ```

---

## 📖 Usage

1. Run the script to see the pirate-themed banner and main menu.
2. Choose an option (1-7) to plunder your desired content.
3. Follow the prompts to enter URLs or set the download directory.

### Menu Options
| Option | Action | Example Input |
|--------|--------|--------------|
| 1 | Pirate a Single Video | `https://youtube.com/watch?v=example` |
| 2 | Batch Pirate Videos | List of URLs, end with `booty confirmed` |
| 3 | Pirate Audio Only (MP3) | `https://youtube.com/watch?v=example` |
| 4 | Change Booty Directory | `/path/to/booty` |
| 5 | Pillage All Videos from a Channel | `https://youtube.com/@channel` |
| 6 | Pillage Channel’s Audio Only | `https://youtube.com/@channel` |
| 7 | Exit | - |

---

## ⚙️ Configuration

- **Default Download Directory**: `./Booty` (created automatically if it doesn’t exist).
- **Audio Quality**: MP3 files are extracted with a default bitrate of 192 kbps.
- **Supported Platforms**: YouTube and Rumble (via `yt-dlp`).

To change the download directory:
1. Select option `4` from the main menu.
2. Enter a new directory path (e.g., `/home/user/downloads`).

---

## 🐬 Example Commands

### Pirate a Single Video
```bash
Select an option (1-7): 1
Enter the video URL to plunder: https://youtube.com/watch?v=example
```

### Batch Download
```bash
Select an option (1-7): 2
Enter video URLs to plunder, one per line. Type 'booty confirmed' when finished:
https://youtube.com/watch?v=video1
https://youtube.com/watch?v=video2
booty confirmed
```

### Pillage a Channel
```bash
Select an option (1-7): 5
Enter the channel URL to plunder (YouTube/Rumble): https://youtube.com/@channel
```

---

## 📜 Code Structure

| File/Function | Purpose |
|---------------|---------|
| `display_banner()` | Shows the pirate-themed ASCII art banner. |
| `download_video()` | Downloads a single video or audio file. |
| `download_channel()` | Downloads all videos or audio from a channel. |
| `main_menu()` | Displays the interactive CLI menu. |
| `option_*` | Handles specific menu options (e.g., `option_single_download`). |

---

## 🛡️ Error Handling

- **Missing Dependencies**: Exits gracefully if `yt-dlp` or `colorama` is not installed.
- **Invalid URLs**: Displays an error and returns to the main menu.
- **Directory Creation**: Creates the download directory if it doesn’t exist or handles errors if creation fails.
- **Keyboard Interrupt**: Exits with a pirate-themed message on `Ctrl+C`.

---

## ⚠️ Notes

- **Dependencies**: Requires `yt-dlp` and `FFmpeg` for full functionality. `colorama` is optional for colored output.
- **Playlists**: Single video downloads ignore playlists (`noplaylist=True`), but channel downloads include all videos.

---

## 📬 Contact

For support or to report issues, contact the BGGG BG Gremlin Group via:
- **GitHub Issues**: [https://github.com/BGGremlin-Group/Simple-Pyrate/]
---

## 🏴‍☠️ Acknowledgments

- Built by the **Background Gremlin Group**.
- Powered by `yt-dlp`, `colorama`, and **FFmpeg**.
- Inspired by the high seas and pirate adventures! 🐬

---

*May the wind be at your back, Captain! 🏴‍☠️*
