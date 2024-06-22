
Encryption and Decryption Programs
This project contains two separate Python programs for encrypting and decrypting messages using the AES (Advanced Encryption Standard) algorithm with GCM (Galois/Counter Mode) for authenticated encryption.

Prerequisites
To run these programs, you need to have Python installed along with the pycryptodome library. You can install pycryptodome using pip:

sh
Copy code
pip install pycryptodome
Files
encrypt.py: A script to encrypt messages.
decrypt.py: A script to decrypt messages.
Usage
Encryption
Run the encrypt.py script:

sh
Copy code
python encrypt.py
Enter the message you want to encrypt. You can type 'exit' to quit the program.

The program will output the encrypted message and the encryption key. Save both the encrypted message and the key securely, as you will need the key to decrypt the message.

Decryption
Run the decrypt.py script:

sh
Copy code
python decrypt.py
Enter the base64 encoded encrypted message and the base64 encoded encryption key when prompted.

The program will output the decrypted message. If decryption fails, an error message will be displayed.

Example
Encryption
sh
Copy code
$ python encrypt.py
Enter your message (or type 'exit' to quit): Hello, World!
Encrypted: YWJjMTIz... (example output)
Encryption Key: dGVzdGtleQ==... (example output)
Decryption
sh
Copy code
$ python decrypt.py
Welcome to the decryption program.
Enter the base64 encoded encrypted message: YWJjMTIz... (example input)
Enter the base64 encoded encryption key: dGVzdGtleQ==... (example input)
Decrypted message: Hello, World!
Security Considerations
The encryption key is randomly generated for each encryption operation, ensuring high security and uniqueness.
AES-GCM mode is used for authenticated encryption, providing both confidentiality and integrity of the encrypted messages.
Ensure the encrypted message and the key are stored and transferred securely.
License
This project is licensed under the MIT License.
