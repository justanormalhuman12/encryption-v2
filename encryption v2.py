from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Encryption function with authenticated encryption (AES-GCM)
def encrypt(plain_text: str) -> (str, str):
    key = get_random_bytes(32)  # Generate a random 256-bit key
    cipher = AES.new(key, AES.MODE_GCM)  # Use AES-GCM mode
    cipher_text, tag = cipher.encrypt_and_digest(plain_text.encode())

    # Combine nonce, tag, and cipher_text for storage/transfer
    encrypted_data = base64.b64encode(cipher.nonce + tag + cipher_text).decode('utf-8')
    
    # Return both the encrypted message and the key (encoded for safe transfer/storage)
    return encrypted_data, base64.b64encode(key).decode('utf-8')

# Main loop to allow input and encryption
def main():
    while True:
        message = input("Enter your message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        encrypted_message, encryption_key = encrypt(message)
        print(f"Encrypted: {encrypted_message}")
        print(f"Encryption Key: {encryption_key}")
        print("\n")

if __name__ == "__main__":
    main()
