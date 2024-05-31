class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def extend_key(self, text):
        extended_key = self.key
        while len(extended_key) < len(text):
            extended_key += self.key
        return extended_key

    def encrypt(self, message):
        extended_key = self.extend_key(message)
        ciphertext = ''
        for i in range(len(message)):
            if message[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                if message[i].islower():
                    encrypted_char = chr((ord(message[i]) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(message[i]) - ord('A') + shift) % 26 + ord('A'))
                ciphertext += encrypted_char
            else:
                ciphertext += message[i]
        return ciphertext

    def decrypt(self, message):
        extended_key = self.extend_key(message)
        plaintext = ''
        for i in range(len(message)):
            if message[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                if message[i].islower():
                    decrypted_char = chr((ord(message[i]) - ord('a') - shift + 26) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(message[i]) - ord('A') - shift + 26) % 26 + ord('A'))
                plaintext += decrypted_char
            else:
                plaintext += message[i]
        return plaintext