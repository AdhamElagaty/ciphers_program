class PlayfairCipher:
    def __init__(self, key):
        self.key = key

    def prepare_text(self, text):
        text = ''.join(char for char in text if char.isalpha() or char.isspace())
        text = text.replace('J', 'I')
        text = text.replace('j', 'i')
        return text

    def prepare_key(self, k):
        k = ''.join(char.upper() for char in k if char.isalpha())
        k = k.replace('J', 'I')
        return k

    def generate_key_square(self):
        key = self.prepare_key((self.key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))
        key_square = []
        for char in key:
            if char not in key_square:
                key_square.append(char)
        return ''.join(key_square)

    def get_char_positions(self, key_square, char):
        row, col = divmod(key_square.index(char), 5)
        return row, col

    def encrypt(self, message):
        message = self.prepare_text(message)
        if len(message) % 2 != 0:
            message += 'X'
        key_square = self.generate_key_square()
        encrypted_text = ""
        for i in range(0, len(message), 2):
            char1, char2 = message[i], message[i + 1]
            if char1.isspace() or char2.isspace():
                encrypted_text += char1 + char2
                continue
            new_char1 = ''
            new_char2 = ''
            row1, col1 = self.get_char_positions(key_square, char1.upper())
            row2, col2 = self.get_char_positions(key_square, char2.upper())
            if row1 == row2:
                new_char1 = key_square[row1 * 5 + (col1 + 1) % 5]
                new_char2 = key_square[row2 * 5 + (col2 + 1) % 5]
            elif col1 == col2:
                new_char1 = key_square[((row1 + 1) % 5) * 5 + col1]
                new_char2 = key_square[((row2 + 1) % 5) * 5 + col2]
            else:
                new_char1 = key_square[row1 * 5 + col2]
                new_char2 = key_square[row2 * 5 + col1]
            if char1.islower():
                encrypted_text += new_char1.lower()
            else:
                encrypted_text += new_char1
            if char2.islower():
                encrypted_text += new_char2.lower()
            else:
                encrypted_text += new_char2
        return encrypted_text

    def decrypt(self, message):
        key_square = self.generate_key_square()
        decrypted_text = ""
        for i in range(0, len(message), 2):
            char1, char2 = message[i], message[i + 1]
            if char1.isspace() or char2.isspace():
                decrypted_text += char1 + char2
                continue
            new_char1 = ''
            new_char2 = ''
            row1, col1 = self.get_char_positions(key_square, char1.upper())
            row2, col2 = self.get_char_positions(key_square, char2.upper())
            if row1 == row2:
                new_char1 = key_square[row1 * 5 + (col1 - 1) % 5]
                new_char2 = key_square[row2 * 5 + (col2 - 1) % 5]
            elif col1 == col2:
                new_char1 = key_square[((row1 - 1) % 5) * 5 + col1]
                new_char2 = key_square[((row2 - 1) % 5) * 5 + col2]
            else:
                new_char1 = key_square[row1 * 5 + col2]
                new_char2 = key_square[row2 * 5 + col1]
            if char1.islower():
                decrypted_text += new_char1.lower()
            else:
                decrypted_text += new_char1
            if char2.islower():
                decrypted_text += new_char2.lower()
            else:
                decrypted_text += new_char2
        if decrypted_text[len(decrypted_text)-1] == 'X':
            decrypted_text = decrypted_text[:-1]
        return decrypted_text
