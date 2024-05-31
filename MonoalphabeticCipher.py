import random

class MonoalphabeticCipher:
    def __init__(self, key):
        self.key = key

    @staticmethod
    def generate_key():
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, message):
        encrypted_text = ""
        for char in message:
            if char.isalpha():
                if char.islower():
                    encrypted_text += self.key[ord(char) - ord('a')].lower()
                elif char.isupper():
                    encrypted_text += self.key[ord(char) - ord('A')].upper()
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, message):
        decrypted_text = ""
        for char in message:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr(self.key.lower().index(char) + ord('a'))
                elif char.isupper():
                    decrypted_text += chr(self.key.upper().index(char) + ord('A'))
            else:
                decrypted_text += char
        return decrypted_text
