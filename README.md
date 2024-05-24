                                                                      **Keylogger with Encryption:**
This project implements a basic keylogger in Python that records key presses and encrypts the log file every 100 key presses. The encryption is performed using the cryptography library with Fernet symmetric encryption.


**Features**
**Keylogging:** Records every key press.
**Encryption:** Encrypts the log file contents every 100 key presses to protect logged data.
**Hidden Files:** Option to hide the keylogger and log files to make them less noticeable.


**Dependencies**
**pynput:** For capturing keyboard events.
**cryptography:** For encrypting log file contents.

You can install these dependencies using pip:
bash code
pip install pynput cryptography

**How to Use**
**Clone the Repository:**

bash code:
git clone https://github.com/yourusername/keylogger-encryption.git
cd keylogger-encryption

**Run the Keylogger:**
bash code:
python keylogger.py

**Encryption Key:**
When you start the keylogger, it will print the encryption key in the console. Save this key securely, as you will need it to decrypt the log file.
