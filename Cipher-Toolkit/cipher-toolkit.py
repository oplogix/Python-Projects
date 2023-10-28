import importlib
print('''
                                                                               ,----,            
                   ,-.----.           ,--,                                   ,/   .`|       ,--. 
  ,----..     ,---,\    /  \        ,--.'|    ,---,.,-.----.               ,`   .'  :   ,--/  /| 
 /   /   \ ,`--.' ||   :    \    ,--,  | :  ,'  .' |\    /  \            ;    ;     /,---,': / ' 
|   :     :|   :  :|   |  .\ :,---.'|  : ',---.'   |;   :    \         .'___,/    ,' :   : '/ /  
.   |  ;. /:   |  '.   :  |: ||   | : _' ||   |   .'|   | .\ :         |    :     |  |   '   ,   
.   ; /--` |   :  ||   |   \ ::   : |.'  |:   :  |-,.   : |: |         ;    |.';  ;  '   |  /    
;   | ;    '   '  ;|   : .   /|   ' '  ; ::   |  ;/||   |  \ :         `----'  |  |  |   ;  ;    
|   : |    |   |  |;   | |`-' '   |  .'. ||   :   .'|   : .  /             '   :  ;  :   '   \   
.   | '___ '   :  ;|   | ;    |   | :  | '|   |  |-,;   | |  \             |   |  '  |   |    '  
'   ; : .'||   |  ':   ' |    '   : |  : ;'   :  ;/||   | ;\  \            '   :  |  '   : |.  \ 
'   | '/  :'   :  |:   : :    |   | '  ,/ |   |    \:   ' | \.'            ;   |.'   |   | '_\.' 
|   :    / ;   |.' |   | :    ;   : ;--'  |   :   .':   : :-'              '---'     '   : |     
 \   \ .'  '---'   `---'.|    |   ,/      |   | ,'  |   |.'                          ;   |,'     
  `---`              `---`    '---'       `----'    `---'                            '---'       ''')
# Main menu
import importlib

# Define a dictionary to map user choices to module names
cipher_modules = {
    "1": "caesar_cipher",
    "2": "rot13_cipher",
    "3": "substitution_cipher",
    "4": "atbash_cipher",
}

# Main menu
while True:
    print("Choose an option:")
    print("1. Caesar Cipher")
    print("2. ROT-13")
    print("3. Substitution Cipher")
    print("4. Atbash Cipher")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in cipher_modules:
        # Load the selected cipher module
        module_name = cipher_modules[choice]
        cipher_module = importlib.import_module(module_name)

        # Get the user's choice (encrypt or decrypt)
        #4user_choice = cipher_module.get_choice()

        # Continue with the selected cipher (e.g., encoding/decoding) using functions from the loaded module
    else:
        print("Invalid choice. Please select a valid option.")
