import math

class RowTranspositionCipher:
    def __init__(self, key):
        self.key = "".join(set(key))

    def create_matrix(self, text, rows, cols, fill_char='X'):
        matrix = [[fill_char] * cols for _ in range(rows)]
        index = 0
        for r in range(rows):
            for c in range(cols):
                if index < len(text):
                    matrix[r][c] = text[index]
                    index += 1
        return matrix

    def get_sorted_key_order(self):
        return sorted((ch, i) for i, ch in enumerate(self.key))

    def encrypt(self, plain_text):
        len_key = len(self.key)
        len_plain = len(plain_text)
        rows = int(math.ceil(len_plain / len_key))
        
        matrix = self.create_matrix(plain_text, rows, len_key)
        sorted_key_order = self.get_sorted_key_order()
        
        cipher_text = ''.join(matrix[r][c] for ch, c in sorted_key_order for r in range(rows))
        return cipher_text

    def decrypt(self, cipher_text):
        len_key = len(self.key)
        len_cipher = len(cipher_text)
        rows = int(math.ceil(len_cipher / len_key))
        
        matrix_new = self.create_matrix('', rows, len_key)
        key_order = [self.key.index(ch) for ch in sorted(self.key)]
        
        index = 0
        for c in key_order:
            for r in range(rows):
                if index < len_cipher:
                    matrix_new[r][c] = cipher_text[index]
                    index += 1
        
        plain_text = ''.join(matrix_new[r][c] for r in range(rows) for c in range(len_key))
        return plain_text.rstrip('X')

