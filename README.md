# Telegram Username Checker

**Made by VRHA**  
discord.gg/vrha

A simple Telegram username checker that does **not** require a phone number, API ID, or login.  
It only checks if usernames are available. It does **not** claim them.

---

## Features

- No phone number needed
- No API ID / API Hash needed
- No Telegram account login required
- Modes: 5l, 5c, 6l, 6c, 7l, 7c, and English words
- Discord webhook notification when an available username is found
- Webhook is saved after the first run (you only enter it once)

---

## How to use

1. Download `telegram_username_checker.py`
2. Install the required library:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python telegram_username_checker.py
   ```
4. First time: enter your Discord webhook URL (it will be saved in `webhook.txt`)
5. Choose a mode (example: `6c` or `words`)
6. The checker starts. Available usernames are sent to your Discord webhook.

---

## Modes

- `5l` = 5 random letters
- `5c` = 5 random letters + numbers
- `6l` = 6 random letters
- `6c` = 6 random letters + numbers
- `7l` = 7 random letters
- `7c` = 7 random letters + numbers
- `words` = English words (5+ letters)

---

## Notes

- This tool only checks availability. It does not claim usernames.
- Telegram usernames must be at least 5 characters long.
- Use at your own risk. Automated checking may go against Telegram's terms of service.
