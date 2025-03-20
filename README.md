# SilverInstaEye - Instagram OSINT Tool

## Overview
Instagram Toolkit is a powerful Python-based tool designed for extracting valuable information from Instagram accounts. With functionalities including downloading posts, retrieving followers/following lists, collecting comments, and fetching email and phone details (where possible), this tool is ideal for research, analysis, and data collection.

## Features
- **Session Management:** Save and restore session data to avoid repeated logins.
- **Extract Contact Information:** Retrieve publicly available phone numbers and emails (masked format).
- **Download Posts:** Bulk download all available posts from a target account.
- **Collect Comments:** Extract and store comments from posts.
- **Retrieve Followers & Following Lists:** Export lists of followers and the accounts being followed.
- **Download Stories Anonymously:** Fetch and save all available stories from a target profile without revealing identity.
- **Identify Posts with User Comments (Dorking):** Extract a list of posts where a specific target has commented.
- **Extract Geolocation from Posts:** Retrieve and analyze geolocation data embedded in posts.
- **Download Instagram Highlights:** Save all highlight stories from a profile.
- **Retrieve Masked Contact Information:** Extract and display phone numbers and email addresses in a masked format (e.g., +1******1234, e******@gmail.com).

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

