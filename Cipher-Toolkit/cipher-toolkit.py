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
while True:
    print("Choose an option:")
    print("1. Caesar Cipher")
    print("2. ROT-13")
    print("3. Substitution Cipher")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Load the Caesar cipher module
        cipher_module = importlib.import_module("ceasar_cipher")
    elif choice == "2":
        # Load the ROT-13 cipher module 
        cipher_module = importlib.import_module("rot13_cipher")
    elif choice == "3":
        # Load the Substitution cipher module
        cipher_module = importlib.import_module("substitution_cipher")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        continue

    # Get the user's choice (encrypt or decrypt)
    user_choice = cipher_module.get_choice()

    # Continue with the selected cipher (e.g., encoding/decoding) using functions from the loaded module
