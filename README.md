# Caesar Cipher - Simple Text Encryption and Decryption

Welcome to the Caesar Cipher project! This Python program allows users to easily encrypt and decrypt messages using one of the simplest and oldest encryption techniques — the Caesar Cipher. Whether you're learning about encryption or exploring fun ways to manipulate text, this project provides a hands-on experience with classic cryptography.

---

## 🔐 What is the Caesar Cipher?

The Caesar Cipher is a substitution cipher, one of the oldest known forms of encryption, named after Julius Caesar, who reportedly used it to protect private messages. In this cipher, each letter in the plaintext (original message) is shifted by a certain number of positions in the alphabet. 

For example, with a shift of 3:
- A becomes D  
- B becomes E  
- C becomes F  

On decryption, the process is reversed, restoring letters back to their original form.

---

## ⚙️ How This Program Works

This Python implementation of the Caesar Cipher allows users to:

- 🔐 **Encrypt** a message by shifting each letter by a user-specified number of positions  
- 🔓 **Decrypt** a message by reversing the shift and recovering the original text

It supports:
- Uppercase and lowercase letters
- Leaves special characters (spaces, punctuation, numbers) unchanged

---

## 🧠 Why Use This Program?

This program is perfect for anyone interested in understanding how basic encryption works. It provides an interactive way to learn how simple ciphers function, and it can even be a starting point for experimenting with more complex cryptographic techniques.

---

## 🚀 How to Run the Program

### 🧑‍💻 Step-by-Step:

```
# 1. Clone this repository
git clone https://github.com/shivatharun07/caesar-cipher.git

# 2. Navigate to the project directory
cd caesar-cipher

# 3. Run the program
python3 caesar_cipher.py

Example Usage:

Welcome to the Caesar Cipher Program!
Do you want to encrypt or decrypt? (type 'exit' to quit): encrypt
Enter your message: Hello, World!
Enter shift value (0-25): 5

Encrypted Message: Mjqqt, Btwqi!

