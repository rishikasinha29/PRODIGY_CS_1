print(" WELCOME TO CAESER CIPHER ENCRYPTION AND DECRYPTION PROGRAM 🔐 ")


def encrypt_message(input_txt , shift_value):
    ciphertext = ""    # encrypted text 
    for character in input_txt:
        if character.isalpha():
            ascii_base = ord('A') if character.isupper() else ord('a')
            shifted_character = chr((ord(character) - ascii_base + shift_value) % 26 + ascii_base)
            ciphertext += shifted_character

        else:
            ciphertext += character
    return ciphertext


def decrypt_message(ciphertext,shift_value):
    return encrypt_message(ciphertext , -shift_value)


def run_caeser_cipher():

    while True:

        choice = input("Do you want to (E)ncrypt or (D)ecrypt ? (Enter 'Q' to Quit): ").upper()
        if choice == 'Q':
            print("Catch you later! Stay Cryptic! 👋 ")
            break

        elif choice not in ['E','D']:
            print("Oops! Invalid choice! Please enter E, D, or Q.")
            continue

        original_txt = input("Type your message here: ")
        shift_val = int(input("Enter your shift value: "))

        if choice == 'E':
            output_text = encrypt_message(original_txt, shift_val)
            print(f"Your encrypted message: {output_text} 🔒")
        elif choice == 'D':
            output_text = decrypt_message(original_txt, shift_val)
            print(f"Your decrypted message: {output_text} 🔒")


if __name__=="__main__":
    run_caeser_cipher()
        
