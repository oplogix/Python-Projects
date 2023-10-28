import random

print(''' (              (          (                      (       )     )  
 )\ )        (  )\ )  *   ))\ )  *   )       *   ))\ ) ( /(  ( /(  
(()/(   (  ( )\(()/(` )  /(()/(` )  /(   ( ` )  /(()/( )\()) )\()) 
 /(_))  )\ )((_)/(_))( )(_))(_))( )(_))  )\ ( )(_))(_)|(_)\ ((_)\  
(_)) _ ((_|(_)_(_)) (_(_()|_)) (_(_())_ ((_|_(_()|_))   ((_) _((_) 
/ __| | | || _ ) __||_   _|_ _||_   _| | | |_   _|_ _| / _ \| \| | 
\__ \ |_| || _ \__ \  | |  | |   | | | |_| | | |  | | | (_) | .` | 
|___/\___/ |___/___/  |_| |___|  |_|  \___/  |_| |___| \___/|_|\_| 
                                                                   
''')
# Define the alphabet.
alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '

def generate_key():
    """Generate a random key."""
    return ''.join(random.sample(alphabet, len(alphabet)))

def get_choice():
    """Prompt the user for their choice: encrypt or decrypt."""
    while True:
        print('''Substitution Cipher
A simple substitution cipher uses a random key to encrypt and decrypt messages.''')
        response = input('Do you want to (enc)rypt or (dec)rypt? > ').lower()
        if response == 'enc':
            return 'encrypt'
        elif response == 'dec':
            return 'decrypt'
        print('Please enter "enc" for encrypt or "dec" for decrypt.')

def get_key():
    """Prompt the user for a key and return it."""
    while True:
        key = input('Enter the key or press Enter to generate a random key: ')
        if key:
            if set(key) == set(alphabet):
                return key
            else:
                print('Invalid key. Key must contain all characters from the alphabet.')
        else:
            return generate_key()

def get_message(mode):
    """Prompt the user for the message to be encoded/decoded and return it."""
    message = input(f'Enter text to be {mode}ed: ')
    return message

def translate_message(message, key, mode):
    """Translate the message using the provided key and mode."""
    translated = ''
    for symbol in message:
        if symbol in alphabet:
            num = alphabet.index(symbol)
            if mode == 'encrypt':
                translated += key[num]
            elif mode == 'decrypt':
                translated += alphabet[key.index(symbol)]
        else:
            translated += symbol
    return translated

def encrypt_message(message, key):
    """Encrypt the given message using the provided key."""
    return translate_message(message, key, 'encrypt')

def decrypt_message(message, key):
    """Decrypt the given message using the provided key."""
    return translate_message(message, key, 'decrypt')

# Main program logic
while True:
    user_choice = get_choice()
    
    if user_choice == 'encrypt':
        key = get_key()
        print('Generated Key:', key)
        message = get_message('encrypt')
        result = encrypt_message(message, key)
        print(f'Encrypted message: {result}')
    elif user_choice == 'decrypt':
        key = get_key()
        message = get_message('decrypt')
        result = decrypt_message(message, key)
        print(f'Decrypted message: {result}')
    
    another_choice = input("Do you want to encode or decode another message (yes/no)? ").lower()
    if another_choice != 'yes':
        print('Returning to the main menu.')
        break
# Still have an issue of reprompting user for enc of dec from the beginning prompts before breaking out of module
