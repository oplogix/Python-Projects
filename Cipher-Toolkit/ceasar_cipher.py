# Intro
print('''
   (              (             (    (        )       (     
   (          (      )\ )    (      )\ )     (    )\ ) )\ )  ( /(       )\ )  
   )\   (     )\    (()/(    )\    (()/(     )\  (()/((()/(  )\()) (   (()/(  
 (((_)  )\ ((((_)(   /(_))((((_)(   /(_))  (((_)  /(_))/(_))((_)\  )\   /(_)) 
 )\___ ((_) )\ _ )\ (_))   )\ _ )\ (_))    )\___ (_)) (_))   _((_)((_) (_))   
((/ __|| __|(_)_\(_)/ __|  (_)_\(_)| _ \  ((/ __||_ _|| _ \ | || || __|| _ \  
 | (__ | _|  / _ \  \__ \   / _ \  |   /   | (__  | | |  _/ | __ || _| |   /  
  \___||___|/_/ \_\ |___/  /_/ \_\ |_|_\    \___||___||_|   |_||_||___||_|_\  
Type 'exit' to exit
''')
print("Welcome to the Caesar Cipher Tool")
print("Type 'exit' to exit")

# Define a function to get user's choice (encode or decode)
def get_choice():
    print('Would you like to encode or decode text?')
    choice = input("Enter your choice (enc/dec): ")
    return choice

# Define the Caesar cipher function for both encoding and decoding
def caesar(text, step):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + step) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + step) % 26) + ord('A'))
        else:
            result += char
    return result

# Define the decoding function
def decode():
    print('Enter the Caesar Cipher message to decode:')
    message = input('> ')

    for key in range(26):
        decoded_message = caesar(message, -key)
        print('Key #{}: {}'.format(key, decoded_message))

# Define the encoding function
def encode():
    plain_text = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar(plain_text, shift)
    print("Encrypted text: ", encrypted_text)

# Main program logic
while True:
    user_choice = get_choice()
    
    if user_choice == "enc":
        encode()
    elif user_choice == "dec":
        decode()
    elif user_choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'enc', 'dec', or 'exit'.")
