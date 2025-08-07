def encrypt(message, shift_value):
    """Encrypt the message using the Caesar cipher."""
    encrypted_message = ""
    for character in message:
        if character.isupper():  # Encrypt uppercase letters
            new_char = chr((ord(character) - ord('A') + shift_value) % 26 + ord('A'))
            encrypted_message += new_char
        elif character.islower():  # Encrypt lowercase letters
            new_char = chr((ord(character) - ord('a') + shift_value) % 26 + ord('a'))
            encrypted_message += new_char
        else:  # Leave non-alphabetic characters unchanged
            encrypted_message += character
    return encrypted_message


def decrypt(message, shift_value):
    """Decrypt the message using the Caesar cipher."""
    return encrypt(message, -shift_value)


def main():
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        operation = input("Do you want to encrypt or decrypt? (type 'exit' to quit): ").lower()
        if operation == 'exit':
            print("Goodbye!")
            break
        
        message = input("Enter your message: ")
        
        # Input validation for shift value
        while True:
            try:
                shift_value = int(input("Enter shift value (0-25): "))
                if 0 <= shift_value <= 25:
                    break
                else:
                    print("Shift value must be between 0 and 25.")
            except ValueError:
                print("Please enter a valid integer.")
        
        if operation == "encrypt":
            encrypted_message = encrypt(message, shift_value)
            print(f"Encrypted Message: {encrypted_message}")
        elif operation == "decrypt":
            decrypted_message = decrypt(message, shift_value)
            print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")


if _name_ == "_main_":
    main()
