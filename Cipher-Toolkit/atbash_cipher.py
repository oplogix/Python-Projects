import random

print('''
                                  (       )  
   (      *   )  (    (     )\ ) ( /(  
   )\   ` )  /(( )\   )\   (()/( )\()) 
((((_)(  ( )(_))((_|(((_)(  /(_)|(_)\  
 )\ _ )\(_(_()|(_)_ )\ _ )\(_))  _((_) 
 (_)_\(_)_   _|| _ )(_)_\(_) __|| || | 
  / _ \   | |  | _ \ / _ \ \__ \| __ | 
 /_/ \_\  |_|  |___//_/ \_\|___/|_||_| 
      ''')
print("Welcome to the Caesar Cipher Tool")
print("Type 'exit' to exit")

# Define the alphabet.
alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

def generate_key():
    """Generate a random key."""
    return ''.join(random.sample(alphabet, len(alphabet)))

def get_choice():
    """Prompt the user for their choice: encrypt or decrypt."""
    while True:
        print('Atbash Cipher')
        response = input('Do you want to (enc)rypt or (dec)rypt? > ').lower()
        if response == 'enc':
            return 'encrypt'
        elif response == 'dec':
            return 'decrypt'
        print('Please enter "enc" for encrypt or "dec" for decrypt.')

def get_message(mode):
    """Prompt the user for the message to be encoded/decoded and return it."""
    message = input(f'Enter text to be {mode}ed: ')
    return message

def atbash_encrypt(message):
    lookup_table = {
        'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
        'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
        'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
        'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
        'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A',' ':' '
    }
    encrypted_message = ''
    for symbol in message:
        if symbol in alphabet:
            if symbol.isupper():
                encrypted_message += lookup_table[symbol]
            else:
                encrypted_message += lookup_table[symbol.upper()].lower()
        else:
            encrypted_message += symbol
    return encrypted_message

def atbash_decrypt(message):
    return atbash_encrypt(message)  # Decryption is the same as encryption in Atbash Cipher

# Main program logic
while True:
    user_choice = get_choice()
    
    if user_choice == 'encrypt':
        message = get_message('encrypt')
        result = atbash_encrypt(message)
        print(f'Encrypted message: {result}')
    elif user_choice == 'decrypt':
        message = get_message('decrypt')
        result = atbash_decrypt(message)
        print(f'Decrypted message: {result}')
    
    another_choice = input("Do you want to encode or decode another message (yes/no)? ").lower()
    if another_choice != 'yes':
        print('Returning to the main menu.')
        break
