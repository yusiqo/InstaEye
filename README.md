# SilverInstaEye - Instagram OSINT Tool

## Overview
SilverInstaEye is a comprehensive OSINT tool for Instagram. It gathers extensive information about the target user. 

## Features
- **Extract Phone number or Mail adress:** The target's phone number or email address is displayed (in a starred format).
- **Download Posts:** Bulk download all available posts from a target account.
- **Collect Comments:** Extract and store comments from posts.
- **Retrieve Followers & Following Lists:** Export lists of followers and the accounts being followed.
- **Download Stories Anonymously:** Fetch and save all available stories from a target profile without revealing identity.
- **Identify Posts with User Comments (Dorking):** Extract a list of posts where a specific target has commented.
- **Extract Geolocation from Posts:** Retrieve and analyze geolocation data embedded in posts.
- **Download Instagram Highlights:** Save all highlight stories from a profile.
## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/silverxpymaster/SilverInstaEye.git
   cd SilverInstaEye
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```sh
   python3 silverinstaeye.py
   ```

## Configuration
- The session is saved in `session.json`. Make sure to keep this file secure.
- Modify API request headers if necessary for stability and efficiency.

## Disclaimer
This tool is intended for educational and research purposes only. Unauthorized use of Instagram data may violate Instagram's policies. Use responsibly.

## Author
- **SilverX**
- Telegram: [t.me/silverxvip](https://t.me/silverxvip)
- YouTube: [silverxcyber](https://www.youtube.com/@silverxcyber)

