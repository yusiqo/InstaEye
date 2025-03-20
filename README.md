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

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install termcolor instagrapi requests beautifulsoup4 colorama
```

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/instagram-toolkit.git
   cd instagram-toolkit
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```sh
   python tool.py
   ```

## Configuration
- The session is saved in `session.json`. Make sure to keep this file secure.
- Modify API request headers if necessary for stability and efficiency.

## Functions Explained
### **Session Management**
```python
def save_session(cl):
    session_data = cl.get_settings()
    with open('session.json', 'w') as file:
        json.dump(session_data, file)
```
- Saves Instagram session data for reuse.

```python
def load_session(cl):
    if os.path.exists('session.json'):
        with open('session.json', 'r') as file:
            session_data = json.load(file)
            cl.set_settings(session_data)
            print("Session restored.")
            return True
    return False
```
- Loads session if previously saved.

### **Extract Contact Information**
```python
def email_ve_telefon_al(api_url, hedef_istifadeci):
```
- Retrieves email and phone number in a masked format.

### **Download Posts**
```python
def postlari_yukle(cl, hedef_istifadeci):
```
- Downloads all posts from a public or followed private account.

### **Collect Comments**
```python
def post_yorumlari_topla(cl, hedef_istifadeci):
```
- Extracts and saves comments from posts.

### **Retrieve Followers & Following Lists**
```python
def izləyiciləri_və_izlədikləri_yazdır(cl, hedef_istifadeci):
```
- Saves followers and following lists to text files.

### **Download Stories Anonymously**
```python
def storiləri_yukle(cl, hedef_istifadeci):
```
- Downloads all available stories without revealing identity.

### **Identify Posts with User Comments (Dorking)**
```python
def hedef_yorum_postlarini_cikar(cl, hedef_istifadeci):
```
- Extracts posts where the target user has commented.

### **Extract Geolocation from Posts**
```python
def post_geolokasyon_cikar(cl, hedef_istifadeci):
```
- Retrieves geolocation data embedded in posts.

### **Download Instagram Highlights**
```python
def highlightlari_yukle(cl, hedef_istifadeci):
```
- Saves all highlight stories from a profile.

## Disclaimer
This tool is intended for educational and research purposes only. Unauthorized use of Instagram data may violate Instagram's policies. Use responsibly.

## Author
- **SilverX**
- Telegram: [t.me/silverxvip](https://t.me/silverxvip)
- YouTube: [silverxcyber](https://www.youtube.com/@silverxcyber)

