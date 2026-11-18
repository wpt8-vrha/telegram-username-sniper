#!/usr/bin/env python3
"""
Telegram Username Checker (No login required)
Made by VRHA
discord.gg/vrha

This version ONLY checks availability. It does NOT claim usernames.
No phone number, API ID or login needed.

Webhook is saved locally after the first run.
"""

import random
import string
import sys
import time
import requests
import os

print("made by VRHA")
print("discord.gg/vrha")
print()
print("Telegram Username Checker (check only - no claiming)")
print()

WEBHOOK_FILE = "webhook.txt"

# Load or ask for webhook
if os.path.exists(WEBHOOK_FILE):
    with open(WEBHOOK_FILE, "r") as f:
        WEBHOOK_URL = f.read().strip()
    print("Webhook loaded from file.")
else:
    WEBHOOK_URL = input("Enter your Discord webhook URL: ").strip()
    if not WEBHOOK_URL.startswith("https://discord.com/api/webhooks/"):
        print("Invalid webhook URL.")
        sys.exit(1)
    with open(WEBHOOK_FILE, "w") as f:
        f.write(WEBHOOK_URL)
    print("Webhook saved.")

print()

print("Choose mode:")
print("  5l  = 5 random letters")
print("  5c  = 5 random letters + numbers")
print("  6l  = 6 random letters")
print("  6c  = 6 random letters + numbers")
print("  7l  = 7 random letters")
print("  7c  = 7 random letters + numbers")
print("  words = English words (5+ letters only)")
mode = input("Mode: ").strip().lower()

# Only words with 5 or more characters (Telegram minimum)
WORD_LIST = [
    "apple", "beach", "cloud", "dream", "earth", "flame", "ghost", "heart",
    "island", "jungle", "knight", "light", "magic", "night", "ocean", "peace",
    "queen", "river", "storm", "tiger", "ultra", "voice", "water", "xenon",
    "youth", "zebra", "alpha", "brave", "crazy", "delta", "eagle", "frost",
    "green", "happy", "ideal", "joker", "karma", "lucky", "money", "noble",
    "omega", "power", "quick", "royal", "super", "truth", "unity", "vivid",
    "wonder", "young", "zenith", "black", "white", "blue", "gold", "silver",
    "diamond", "shadow", "phoenix", "dragon", "wolf", "lion", "bear", "shark",
    "falcon", "thunder", "fire"
]

length = 5
use_words = False
charset = string.ascii_lowercase

if mode == "5l":
    length = 5
    charset = string.ascii_lowercase
    print("Mode: 5l (random letters only)")
elif mode == "5c":
    length = 5
    charset = string.ascii_lowercase + string.digits
    print("Mode: 5c (random letters + numbers)")
elif mode == "6l":
    length = 6
    charset = string.ascii_lowercase
    print("Mode: 6l (random letters only)")
elif mode == "6c":
    length = 6
    charset = string.ascii_lowercase + string.digits
    print("Mode: 6c (random letters + numbers)")
elif mode == "7l":
    length = 7
    charset = string.ascii_lowercase
    print("Mode: 7l (random letters only)")
elif mode == "7c":
    length = 7
    charset = string.ascii_lowercase + string.digits
    print("Mode: 7c (random letters + numbers)")
elif mode == "words":
    print("Mode: English words (5+ letters)")
    use_words = True
else:
    print("Invalid mode.")
    sys.exit(1)

print("\nStarting checker... Press Ctrl+C to stop.")
print("Discord webhook notification enabled.\n")

checked = 0
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

def send_discord_notification(username):
    """Send a message via Discord webhook when a free username is found."""
    try:
        payload = {
            "content": f"**Telegram username AVAILABLE:** `{username}`"
        }
        r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if r.status_code in (200, 204):
            print(f"  -> Discord webhook sent for {username}")
        else:
            print(f"  -> Webhook failed: {r.status_code} - {r.text[:150]}")
    except Exception as e:
        print(f"  -> Discord notify error: {e}")

try:
    while True:
        if use_words:
            username = random.choice(WORD_LIST)
        else:
            username = ''.join(random.choice(charset) for _ in range(length))

        checked += 1

        try:
            r = session.get(f"https://t.me/{username}", timeout=8, allow_redirects=True)
            text = r.text

            # Better detection: presence of tgme_page_title means a public profile exists = taken
            if "tgme_page_title" in text:
                print(f"[{checked}] Taken: {username}")
            else:
                print(f"[{checked}] AVAILABLE: {username}")
                send_discord_notification(username)

        except requests.RequestException as e:
            print(f"[{checked}] Request error: {e}")
            time.sleep(1)

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nStopped by user.")
