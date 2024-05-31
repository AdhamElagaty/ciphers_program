class PolyalphabeticCipher:
    def __init__(self, key):
        self.key_rules = self.integer_to_list(key)

    def integer_to_list(self, integer):
        return [int(digit) for digit in str(integer)]

    def encrypt(self, message):
        encrypted_text = ""
        if len(message) < len(self.key_rules):
            len_of_key = len(message)
        else:
            len_of_key = len(self.key_rules)
        for i, char in enumerate(message):
            if char.isalpha():
                shift = self.key_rules[i % len_of_key]
                if char.isupper():
                    encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
                else:
                    encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    def decrypt(self, message):
        decrypted_text = ""
        if len(message) < len(self.key_rules):
            len_of_key = len(message)
        else:
            len_of_key = len(self.key_rules)
        for i, char in enumerate(message):
            if char.isalpha():
                shift = self.key_rules[i % len_of_key]
                if char.isupper():
                    decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
                else:
                    decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text
