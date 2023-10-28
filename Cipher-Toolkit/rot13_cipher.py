# Intro
print('''
 (        )                           
 )\ )  ( /(   *   )         )      )  
(()/(  )\())` )  /(      ( /(   ( /(  
 /(_))((_)\  ( )(_))___  )\())  )\()) 
(_))    ((_)(_(_())|___|((_)\  ((_)\  
| _ \  / _ \|_   _|      / (_)|__ (_) 
|   / | (_) | | |        | |   |_ \   
|_|_\  \___/  |_|        |_|  |___/   
                                      
Type 'exit' to exit
''')

# Define a function to get the user's choice (encode or decode)
def get_choice():
    print('Would you like to encode or decode text?')
    choice = input("Enter your choice (enc/dec): ")
    return choice

# Get the user's choice
user_choice = get_choice()

# Define the ROT-13 function for both encoding and decoding
def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char
    return result

# Define the decoding function
def decode():
    print('Enter the ROT-13 message to decode:')
    message = input('> ')
    decoded_message = rot13(message)
    print('Decoded message: ', decoded_message)

# Define the encoding function
def encode():
    plain_text = input("Enter the plaintext: ")
    encoded_text = rot13(plain_text)
    print("Encoded text: ", encoded_text)

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
