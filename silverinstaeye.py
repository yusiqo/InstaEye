from termcolor import colored
from instagrapi import Client
from googlesearch import search
import os
import time
import requests
import json
import re
import argparse
from bs4 import BeautifulSoup
from colorama import Fore

os.system("cls || clear")
print(colored("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
███████╗██╗██╗    ██╗   ██╗███████╗██████╗ ██╗███╗   ██╗███████╗████████╗ █████╗ ███████╗██╗   ██╗███████╗
██╔════╝██║██║    ██║   ██║██╔════╝██╔══██╗██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝
███████╗██║██║    ██║   ██║█████╗  ██████╔╝██║██╔██╗ ██║███████╗   ██║   ███████║█████╗   ╚████╔╝ █████╗  
╚════██║██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔══╝    ╚██╔╝  ██╔══╝  
███████║██║███████╗╚████╔╝ ███████╗██║  ██║██║██║ ╚████║███████║   ██║   ██║  ██║███████╗   ██║   ███████╗
╚══════╝╚═╝╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                                                                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⢰⡆⢘⣆⠀⠀⡆⠀⢸⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣆⣧⡤⠾⢷⡚⠛⢻⣏⢹⡏⠉⣹⠟⡟⣾⠳⣼⢦⣀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣄⡬⢷⣝⢯⣷⢤⣘⣿⣦⣼⣿⣾⣷⣼⣽⣽⣿⣯⡾⢃⣠⣞⠟⠓⢦⣀⠆⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠲⣄⣤⣞⡉⠛⢶⣾⡷⠟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⢿⡛⠻⠿⣥⣤⣶⠞⠉⢓⣤⡴⢁⠄⠀⠀⠀⠀⠀
⠀⠀⠀⣄⣠⠞⠉⢛⣻⡿⠛⠁⠀⣸⠯⠈⠀⠁⣴⣿⣿⣿⡶⠤⠽⣇⠈⣿⠀⠀⠈⠙⠻⢶⣾⣻⣭⠿⢫⣀⣴⡶⠃⠀⠀
⠀⢤⣀⣜⣉⣩⣽⠿⠋⠀⠀⠀⠀⣿⠈⠀⠀⢸⣿⣿⣿⣿⣀⠀⠀⠸⠇⢸⡇⠀⠀⠀⠀⠀⠘⠛⢶⣶⣾⣻⡯⠄⠀⣠⠄
⠀⠤⠬⢭⣿⣿⠋⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⢿⣿⣿⣿⡿⠋⠁⠀⠀⣼⠁⠀⠀⠀⠀⠀⢀⣴⣫⣏⣙⠛⠒⠚⠋⠁⠀
⡔⢀⡵⠋⢧⢹⡀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⣠⣾⣿⡛⠛⠛⠓⠦⠀⠀⠀⠀
⣇⠘⠳⠦⠼⠧⠷⣄⣀⠀⠀⠀⠀⠀⠀⠳⢤⣀⠀⠀⠀⠀⠀⢀⣠⠾⠃⠀⠀⠀⣀⣴⣻⣟⡋⠉⠉⢻⠶⠀⠀⠀⠀⠀⠀
⠈⠑⠒⠒⠀⠀⢄⣀⡴⣯⣵⣖⣦⠤⣀⣀⣀⠉⠙⠒⠒⠒⠚⠉⢁⣀⣠⢤⣖⣿⣷⢯⡉⠉⠙⣲⠞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠣⢤⡞⠉⢉⡿⠒⢻⢿⡿⠭⣭⡭⠿⣿⡿⠒⠻⣯⡷⡄⠉⠳⣬⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠺⠤⣄⣠⡏⠀⠀⡿⠀⠀⠘⡾⠀⢀⣈⡧⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠒⠓⠒⠒⠚⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


                          Author: SilverX                Tg: t.me/silverxvip
""",'red'))

Qara = '\033[30m'
Qirmizi = '\033[1;31m'
Yasil = '\033[1;32m'
Sari = '\033[1;33m'
Mavi = '\033[1;34m'
Magenta = '\033[1;35m'
Cy = '\033[1;36m'
Aq = '\033[1;37m'

SESSION_FILE = 'session.json'

def save_session(cl):
    session_data = cl.get_settings()
    with open(SESSION_FILE, 'w') as file:
        json.dump(session_data, file)

def load_session(cl):
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            session_data = json.load(file)
            cl.set_settings(session_data)
            print(f"{Aq}[ {Yasil}+ {Aq}] The session has been restored.")
            return True
    else:
        print(f"{Aq}[ {Qirmizi}! {Aq}] Session file not found, please log in again.")
        return False


def email_ve_telefon_al(api_url, hedef_istifadeci):
    sorgu_bashliqlari = {
        'accept-language': 'en-US;q=1.0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
    }
    sorgu_melumatlari = {"q": hedef_istifadeci}

    try:
        cavab = requests.post(api_url, headers=sorgu_bashliqlari, data=sorgu_melumatlari)
        cavab.raise_for_status()
        try:
            cavab_json = cavab.json()
        except json.decoder.JSONDecodeError:
            print(Fore.RED + f"JSON parse error occurred: The data is not in the correct format.")
            return 'False', 'False'
        
        telefon = cavab_json.get('phone_number', 'False')
        email = cavab_json.get('email', 'False')

        return telefon, email

    except requests.RequestException as xeta:
        print(Fore.RED + f"An error occurred while retrieving the phone number and email: {xeta}")
        return 'False', 'False'


def postlari_yukle(cl, hedef_istifadeci):
    try:
        user = cl.user_info_by_username(hedef_istifadeci)

        if user.is_private:
            print(f"[!] {hedef_istifadeci} This is a personal account.")
            following_list = cl.user_following(cl.user_id)
            if user.pk not in following_list:
                print(f"[X] {hedef_istifadeci} This is a personal account, and you are not following it.")
                return
            else:
                print(f"[+] {hedef_istifadeci} This is a personal account, but it is being followed. The posts are being loaded...")

        media_list = cl.user_medias(user.pk, amount=0)

        if not media_list:
            print(f"[!] {hedef_istifadeci} The user has no posts.")
            return

        qovluq_adi = hedef_istifadeci
        os.makedirs(qovluq_adi, exist_ok=True)

        print(f"[+] {hedef_istifadeci} The user's posts are being loaded..")

        for idx, media in enumerate(media_list):
            try:
                media_url = None
                if media.media_type == 1:
                    media_url = media.thumbnail_url
                    dosya_adi = f"post_{idx + 1}.jpg"
                elif media.media_type == 2:
                    media_url = media.video_url
                    dosya_adi = f"post_{idx + 1}.mp4"
                
                if not media_url:
                    raise ValueError(f"Post {idx + 1} Not Uploaded")
                
                fayl_yolu = os.path.join(qovluq_adi, dosya_adi)

                response = requests.get(media_url, stream=True)
                response.raise_for_status()
                
                with open(fayl_yolu, 'wb') as fayl:
                    for chunk in response.iter_content(chunk_size=8192):
                        fayl.write(chunk)

                print(f"[+] Post {idx + 1} : {fayl_yolu}")
                time.sleep(1)
            except Exception as e:
                print(f"[X] Post {idx + 1} - An error occurred while uploading the post.: {str(e)}")

        print(f"[+] {hedef_istifadeci} All posts of the user are stored in folder '{qovluq_adi}'")

    except Exception as e:
        print(f"[X] An error occurred while uploading the posts: {str(e)}")


def post_yorumlari_topla(cl, hedef_istifadeci):
    try:
        user = cl.user_info_by_username(hedef_istifadeci)
        media_list = cl.user_medias(user.pk, amount=0)

        if not media_list:
            print(f"[!] {hedef_istifadeci} The user has no posts.")
            return

        yorum_fayl_adi = f"{hedef_istifadeci}_comments.txt"
        with open(yorum_fayl_adi, 'w', encoding='utf-8') as fayl:
            fayl.write(f"============================== {hedef_istifadeci} Comments ==============================")

            print(f"[+] {hedef_istifadeci} Comments are being collected from the user's posts...")

            for idx, media in enumerate(media_list):
                try:
                    yorumlar = cl.media_comments(media.pk, amount=0)

                    if not yorumlar:
                        print(f"[!] Post {idx + 1} does not have comments.")
                        continue

                    fayl.write(f"Post {idx + 1}:")
                    for yorum in yorumlar:
                        fayl.write(f"  - {yorum.user.username}: {yorum.text}\n")
                    fayl.write("\n")

                    print(f"[+] Post {idx + 1} comments collected.")
                except Exception as e:
                    print(f"[X] Post {idx + 1} An error occurred while loading comments: {str(e)}")

        print(f"[+] All comments were written to the '{yorum_fayl_adi}' file.")
    except Exception as e:
        print(f"[X] An error occurred while uploading the comments: {str(e)}")

def izleyicileri_ve_izlediklerini_yazdir(cl, hedef_istifadeci, amount=0):
    try:
        user = cl.user_info_by_username(hedef_istifadeci)
        print(f"{Aq}[ {Yasil}+ {Aq}] Collecting followers and following of {hedef_istifadeci}...")

        izleyiciler = cl.user_followers(user.pk, amount=amount)
        izleyiciler_fayl = f"{hedef_istifadeci}_followers.txt"
        with open(izleyiciler_fayl, 'w', encoding='utf-8') as fayl:
            fayl.write(f"============================== {hedef_istifadeci} Followers ==============================\n")
            for idx, follower in enumerate(izleyiciler.values(), start=1):
                fayl.write(f"{idx}. {follower.username}\n")
        print(f"{Aq}[ {Yasil}+ {Aq}] Followers of {hedef_istifadeci} saved to '{izleyiciler_fayl}'.")

        izledikleri = cl.user_following(user.pk, amount=amount)
        izledikleri_fayl = f"{hedef_istifadeci}_following.txt"
        with open(izledikleri_fayl, 'w', encoding='utf-8') as fayl:
            fayl.write(f"============================== {hedef_istifadeci} Following ==============================\n")
            for idx, following in enumerate(izledikleri.values(), start=1):
                fayl.write(f"{idx}. {following.username}\n")
        print(f"{Aq}[ {Yasil}+ {Aq}] Following of {hedef_istifadeci} saved to '{izledikleri_fayl}'.")

    except Exception as e:
        print(f"{Aq}[ {Qirmizi}! {Aq}] An error occurred while fetching followers and following: {str(e)}")


def storiləri_yukle(cl, hedef_istifadeci):
    try:
        user = cl.user_info_by_username(hedef_istifadeci)

        if user.is_private:
            print(f"{Aq}[ {Sari}! {Aq}] {hedef_istifadeci} private accaunt.")
            following_list = cl.user_following(cl.user_id)
            if user.pk not in following_list:
                print(f"{Aq}[ {Qirmizi}! {Aq}] {hedef_istifadeci} It is a private account and you are not following it.")
                return
            else:
                print(f"{Aq}[ {Yasil}+ {Aq}] {hedef_istifadeci} It is a private account, but it is being followed.Stories are being downloaded...")

        stories = cl.user_stories(user.pk)

        if not stories:
            print(f"{Aq}[ {Sari}! {Aq}] {hedef_istifadeci} The user has no stories")
            return

        qovluq_adi = f"{hedef_istifadeci}_stories"
        if not os.path.exists(qovluq_adi):
            os.mkdir(qovluq_adi)

        print(f"{Aq}[ {Yasil}+ {Aq}] {hedef_istifadeci} The user's stories are being downloaded...")

        for idx, story in enumerate(stories):
            try:
                media_url = story.thumbnail_url if story.media_type == 1 else story.video_url
                fayl_yolu = os.path.join(qovluq_adi,
                                         f"story_{idx + 1}.jpg" if story.media_type == 1 else f"story_{idx + 1}.mp4")

                with open(fayl_yolu, 'wb') as fayl:
                    fayl.write(requests.get(media_url).content)

                print(f"{Aq}[ {Yasil}+ {Aq}] Story {idx + 1} Downloaded: {fayl_yolu}")
                time.sleep(1)
            except Exception as e:
                print(f"{Aq}[ {Qirmizi}! {Aq}] An error occurred while loading Story {idx + 1}: {str(e)}")

        print(
            f"{Aq}[ {Yasil}+ {Aq}] All stories of {hedef_istifadeci} have been saved in the '{qovluq_adi}' folder.")

    except Exception as e:
        print(f"{Aq}[ {Qirmizi}! {Aq}] An error occurred while loading the stories: {str(e)}")


def dorkla_melumat_topla(hedef_istifadeci):
    google_dork = f"site:instagram.com intext:{hedef_istifadeci}"

    try:
        links = [url for url in search(google_dork, num_results=10, unique=True) if "https://www.instagram.com/" in url]

        if not links:
            print("[!] Heç bir nəticə tapılmadı.")
            return

        fayl_adi = f"{hedef_istifadeci}_dork_links.txt"
        with open(fayl_adi, 'w', encoding='utf-8') as file:
            file.write("The following Instagram links were found:\n")
            for link in links:
                file.write(link + '\n')

        print(f"[+] The results have been written to the file'{fayl_adi}'")

    except Exception as e:
        print(f"[!] An error occurred: {e}")

def geo_melumatlari_topla(cl, hedef_istifadeci):
    try:
        user = cl.user_info_by_username(hedef_istifadeci)
        try:
            media_list = cl.user_medias_v1(user.pk, 20)
        except Exception:
            print(f"{Aq}[ {Qirmizi}! {Aq}] Media data could not be retrieved.")
            return

        if not media_list:
            print(f"{Aq}[ {Sari}! {Aq}] {hedef_istifadeci} has no posts.")
            return

        geo_fayl_adi = f"{hedef_istifadeci}_geo_data.txt"
        with open(geo_fayl_adi, 'w', encoding='utf-8') as fayl:
            fayl.write(f"============================== {hedef_istifadeci} Geo Data ==============================")
            
            print(f"{Aq}[ {Yasil}+ {Aq}] Geo data is being collected from the posts of {hedef_istifadeci}")

            for idx, media in enumerate(media_list):
                try:
                    if media.location:
                        location = media.location
                    else:
                        continue
                    
                    try:
                        location_details = cl.location_info_v1(location.pk)
                    except Exception:
                        try:
                            location_details = cl.location_info_a1(location.pk)
                        except Exception:
                            location_details = None

                    fayl.write(f"\nPost {idx + 1}:")
                    fayl.write(f"\n  - Location: {location.name}")
                    fayl.write(f"\n  - Latitude: {location.lat}")
                    fayl.write(f"\n  - Longitude: {location.lng}")
                    
                    if location_details:
                        fayl.write(f"\n  - Name: {location_details.name}")
                        fayl.write(f"\n  - Address: {location_details.address if location_details.address else 'No data available'}")
                        fayl.write(f"\n  - City: {location_details.city if location_details.city else 'No data available'}")
                    fayl.write("\n")

                    print(f"{Aq}[ {Yasil}+ {Aq}] Geo data collected for Post {idx + 1}.")
                except Exception:
                    continue
        
        print(f"\n{Aq}[ {Yasil}+ {Aq}] All geo data has been written to the '{geo_fayl_adi}' file.")
    except Exception:
        print(f"{Aq}[ {Qirmizi}! {Aq}] An unexpected error occurred.")

def highlightlari_yukle(cl, hedef_istifadeci):
    try:        
        user = cl.user_info_by_username(hedef_istifadeci)
        highlights = cl.user_highlights(user.pk)
        
        if not highlights:
            print(f"{Aq}[ {Sari}! {Aq}] {hedef_istifadeci} Highlights not found.")
            return
        
        os.makedirs(f"highlights/{hedef_istifadeci}", exist_ok=True)
        
        for highlight in highlights:
            highlight_info = cl.highlight_info(highlight.pk)
            highlight_folder = f"highlights/{hedef_istifadeci}/{highlight.title}"
            os.makedirs(highlight_folder, exist_ok=True)
            
            for idx, item in enumerate(highlight_info.items):
                try:
                    media_url = item.video_url if item.video_url else item.thumbnail_url
                    ext = "mp4" if item.video_url else "jpg"
                    file_path = os.path.join(highlight_folder, f"highlight_{idx + 1}.{ext}")
                    
                    response = requests.get(media_url, stream=True)
                    if response.status_code == 200:
                        with open(file_path, "wb") as f:
                            for chunk in response.iter_content(1024):
                                f.write(chunk)
                        print(f"{Aq}[ {Yasil}+ {Aq}] {highlight.title} - highlight {idx + 1} has been downloaded.")
                    else:
                        print(f"{Aq}[ {Qirmizi}! {Aq}] {highlight.title} - highlight {idx + 1} could not be downloaded.")
                except Exception as e:
                    print(f"{Aq}[ {Qirmizi}! {Aq}] Xəta: {e}")
        
        print(f"\n{Aq}[ {Yasil}+ {Aq}] All highlights have been downloaded.")
    except Exception as e:
        print(f"{Aq}[ {Qirmizi}! {Aq}] An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Instagram User Information and Content Downloader")
    parser.add_argument('-u', '--username', required=True, help="Instagram username to target")
    parser.add_argument('-informations', action='store_true', help="Fetch user information(number,mail,id,bio, etc...)")
    parser.add_argument('-posts', action='store_true', help="Download user posts")
    parser.add_argument('-stories', action='store_true', help="Download user stories")
    parser.add_argument('-highlights', action='store_true', help="Download user highlights")
    parser.add_argument('-dorks', action='store_true', help="Collect information using Google dorks")
    parser.add_argument('-comments', action='store_true', help="Collect comments from user posts")
    parser.add_argument('-geo', action='store_true', help="Collect geo data from user posts")
    parser.add_argument('-follow', action='store_true', help="Collect followers and following list")

    args = parser.parse_args()

    cl = Client()
    if not load_session(cl):
        IstifadeciAdi = input(f"\n[ {Yasil}+ {Aq}] Enter your Instagram Username: {Qirmizi}")
        Sifre = input(f"[ {Yasil}+ {Aq}] Enter your Instagram Password: {Qirmizi}")
        try:
            cl.login(IstifadeciAdi, Sifre)
            print(f"{Aq}[ {Yasil}+ {Aq}] Login completed successfully!")
            save_session(cl)
        except Exception as e:
            print(f"{Aq}[ {Qirmizi}! {Aq}] An error occurred during login: {str(e)}")
            return

    hedef_istifadeci = args.username

    if args.informations:
        try:
            melumatlar = ['68', '74', '74', '70', '73', '3A', '2F', '2F', '69', '2E', '69', '6E', '73', '74', '61',
                          '67', '72', '61', '6D', '2E', '63', '6F', '6D', '2F', '61', '70', '69', '2F', '76', '31',
                          '2F', '75', '73', '65', '72', '73', '2F', '6C', '6F', '6F', '6B', '75', '70', '2F']
            melumat_str = ''.join([chr(int(x, 16)) for x in melumatlar])
            api_url = melumat_str

            print(f"\n{Aq}[ {Yasil}+ {Aq}] Closing target: {hedef_istifadeci}")
            telefon, email = email_ve_telefon_al(api_url, hedef_istifadeci)

            user = cl.user_info_by_username(hedef_istifadeci)

            print(f"Username              : {user.username}")
            print(f"Full Name               : {user.full_name}")
            print(f"Id                    : {user.pk}")
            print(f"Bio                   : {user.biography}")
            print(f"Profile Link          : {user.external_url}")
            print(f"Is it a private account?      : {user.is_private}")
            print(f"Is it a business account?    : {user.is_business}")
            print(f"Phone Number       : {telefon}")
            print(f"Email                : {email}")
            print(f"Followers Count      : {user.follower_count}")
            print(f"Following Count      : {user.following_count}")
            print(f"Number of Posts        : {user.media_count}")
            print("-" * 50)

            txt_fayl = f"accaunt_{hedef_istifadeci}.txt"
            with open(txt_fayl, 'w', encoding='utf-8') as fayl:
                fayl.write(f"============================== ACCAUNT INFORMATIONS ===============================\n")
                fayl.write(f"Username              : {user.username}\n")
                fayl.write(f"Full Name               : {user.full_name}\n")
                fayl.write(f"Id                    : {user.pk}\n")
                fayl.write(f"Bio                   : {user.biography}\n")
                fayl.write(f"Profile Link          : {user.external_url}\n")
                fayl.write(f"Is it a private account?      : {user.is_private}\n")
                fayl.write(f"Is it a business account?    : {user.is_business}\n")
                fayl.write(f"Phone Number       : {telefon}\n")
                fayl.write(f"Email                : {email}\n")
                fayl.write(f"Followers Count      : {user.follower_count}\n")
                fayl.write(f"Following Count      : {user.following_count}\n")
                fayl.write(f"Number of Posts        : {user.media_count}\n")

            print(f"\n{Aq}[ {Yasil}+ {Aq}] Information about {hedef_istifadeci} has been saved in the {txt_fayl} file.")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {str(e)}")

    if args.posts:
        postlari_yukle(cl, hedef_istifadeci)

    if args.stories:
        storiləri_yukle(cl, hedef_istifadeci)

    if args.highlights:
        highlightlari_yukle(cl, hedef_istifadeci)

    if args.dorks:
        dorkla_melumat_topla(hedef_istifadeci)

    if args.comments:
        post_yorumlari_topla(cl, hedef_istifadeci)

    if args.geo:
        geo_melumatlari_topla(cl, hedef_istifadeci)

    if args.follow:
        izleyicileri_ve_izlediklerini_yazdir(cl, hedef_istifadeci)

if __name__ == "__main__":
    main()
