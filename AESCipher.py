from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESCipher:
    def __init__(self, key):
        self.key = key
        
    @staticmethod
    def generate_key():
        return get_random_bytes(16)

    def encrypt(self, message):
        cipher = AES.new(self.key, AES.MODE_ECB)
        padded_message = pad(message.encode(), AES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return ciphertext.hex()

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext_bytes = bytes.fromhex(ciphertext)
        decrypted_message = cipher.decrypt(ciphertext_bytes)
        unpadded_message = unpad(decrypted_message, AES.block_size)
        return unpadded_message.decode()