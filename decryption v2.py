from Crypto.Cipher import AES
import base64

# Decryption function with authenticated encryption (AES-GCM)
def decrypt(encrypted_data: str, encoded_key: str) -> str:
    encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))
    key = base64.b64decode(encoded_key.encode('utf-8'))

    # Extract the nonce, tag, and cipher_text from the encrypted data
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    cipher_text = encrypted_data[32:]

    # Initialize the cipher
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # Decrypt and verify the cipher text
    plain_text = cipher.decrypt_and_verify(cipher_text, tag)

    return plain_text.decode('utf-8')

# Main function to prompt for input and perform decryption
def main():
    print("Welcome to the decryption program.")
    encrypted_message = input("Enter the base64 encoded encrypted message: ")
    encryption_key = input("Enter the base64 encoded encryption key: ")

    try:
        decrypted_message = decrypt(encrypted_message, encryption_key)
        print(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    main()
