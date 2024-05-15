# Advanced Keylogger

## Description
Advanced Keylogger is a Python-based application that logs keystrokes, captures screenshots, copies clipboard content, and sends them via email.

## Features
- **Keylogging**: Records all keystrokes and stores them in a file.
- **Clipboard Monitoring**: Captures content copied to the clipboard and saves it in a separate file.
- **Screenshot Capture**: Takes screenshots periodically and saves them as images.
- **Email Notification**: Sends logged keystrokes, clipboard content, and screenshots to a specified email address.

## Requirements
- Python 3.x
- `pynput` library
- `pyperclip` library
- `smtplib` library
- `mss` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Advanced-Keylogger.git
   ```
2. Install the required libraries:
   ```bash
   pip install pynput pyperclip mss
   ```

## Usage
1. Run the `keylogger.py` script:
   ```bash
   python keylogger.py
   ```
    2. The keylogger will start running in the background.
3. Press `Esc` key to stop the keylogger.
4. After stopping, the recorded keystrokes, clipboard content, and screenshots will be sent to the specified email address.

## Configuration
- Modify the `sender_email`, `password`, and `receiver_mail` variables in the `keylogger.py` file to configure email settings.
- Adjust the frequency of screenshots by modifying the `screenshot()` function call in the main block.

## Disclaimer
This project is intended for educational purposes only. Misuse of this software may violate privacy laws
