# Cipher Toolkit

Welcome to the Cipher Toolkit, a Python program that provides a collection of ciphers for encrypting and decrypting messages. This toolkit includes various ciphers, and you can easily add more as needed.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Included Ciphers](#included-ciphers)
- [Adding New Ciphers](#adding-new-ciphers)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the Cipher Toolkit, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git.

   ```sh
   git clone https://github.com/your-username/cipher-toolkit.git

2. **Navigate to the Directory**: Change your current directory to the cloned repository.

   ```sh
   cd cipher-toolkit

3. **Run the Toolkit**: Run the cipher_toolkit.py script to access the ciphers.

   ```sh
   python cipher_toolkit.py
   
## Usage
Upon running the cipher_toolkit.py script, you will be presented with a main menu where you can choose from the available ciphers and perform encryption or decryption. The toolkit is designed to be user-friendly and allows you to interact with various ciphers effortlessly.

## Included Ciphers
The Cipher Toolkit includes the following ciphers:

1. **Caesar Cipher**: A simple substitution cipher that shifts characters in the alphabet by a fixed number of positions.

2. **ROT-13 Cipher**: A specific case of the Caesar cipher, which shifts characters by 13 positions. It's often used for basic text obfuscation.

3. **Substitution Cipher**: Encrypts and decrypts messages by substituting each character in the input message with the corresponding character from a user-defined or randomly generated key.

4. **Atbash Cipher**: Substitution cipher that replaces each letter in the plaintext with its counterpart from the reverse end of the alphabet, preserving case and non-alphabet characters. 

## Adding New Ciphers
The Cipher Toolkit is designed to be extensible. If you'd like to add a new cipher, follow these steps:

1. Create a new Python module for your cipher (e.g., my_cipher.py) and implement the cipher's encryption and decryption logic within the module.

2. In the cipher_toolkit.py script, use importlib to dynamically load your new cipher module based on user choice in the main menu.

3. Update the main menu to include your new cipher as an option.

4. With this structure, you can easily expand the toolkit with additional ciphers of your choice.

## Contributing
We welcome contributions to the Cipher Toolkit. If you'd like to add new ciphers, improve existing ones, or make other enhancements, feel free to open an issue or submit a pull request. Your contributions are appreciated!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
