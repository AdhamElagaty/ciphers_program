from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class DECCipher:
    def __init__(self, key):
        self.key = key
        
    @staticmethod
    def generate_key():
        return get_random_bytes(8)

    def encrypt(self, message):
        cipher = DES.new(self.key, DES.MODE_ECB)
        padded_message = pad(message.encode(), DES.block_size)
        ciphertext = cipher.encrypt(padded_message)
        return ciphertext.hex()

    def decrypt(self, ciphertext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext_bytes = bytes.fromhex(ciphertext)
        decrypted_message = cipher.decrypt(ciphertext_bytes)
        unpadded_message = unpad(decrypted_message, DES.block_size)
        return unpadded_message.decode()