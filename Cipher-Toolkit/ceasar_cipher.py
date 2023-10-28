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
by Oplogix                                                                             
''')
print("Welcome to the Caesar Cipher Tool")
print("Type 'exit' to exit")

# Define a function to get user's choice (encode or decode)
def get_choice():
    print('Would you like to encode or decode text?')
    choice = input("Enter your choice (enc/dec): ")
    return choice

# Get the user's choice
user_choice = get_choice()

# Define the Caesar cipher functions for both encoding and decoding
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
    if user_choice == "dec":
        decode()
    elif user_choice == "enc":
        encode()
    elif user_choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'enc' or 'dec'.")

    # Ask the user if they want to continue
    user_choice = input("Do you want to encode or decode another message (enc/dec) or exit? ")
    if user_choice == "exit":
        print("Goodbye!")
        break
