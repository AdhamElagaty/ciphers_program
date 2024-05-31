class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_text += chr((ord(char) - ord('a') + self.shift) % 26 + ord('a'))
                elif char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + self.shift) % 26 + ord('A'))
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr((ord(char) - ord('a') - self.shift) % 26 + ord('a'))
                elif char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - self.shift) % 26 + ord('A'))
            else:
                decrypted_text += char
        return decrypted_text
