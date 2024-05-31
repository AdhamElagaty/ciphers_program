class RailFenceCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        result = ""
        rail_fence = self._generateRailFence(len(message))

        for i in range(self.key):
            for j in range(len(message)):
                if rail_fence[i][j] == 1:
                    result += message[j]

        return result

    def decrypt(self, message):
        result = ""
        rail_fence = self._generateRailFence(len(message))

        idx = 0

        for i in range(self.key):
            for j in range(len(message)):
                if rail_fence[i][j] == 1:
                    rail_fence[i][j] = message[idx]
                    idx += 1

        idx = 0
        for j in range(len(message)):
            for i in range(self.key):
                if rail_fence[i][j] != 0:
                    result += rail_fence[i][j]
                    idx += 1

        return result

    def _generateRailFence(self, length):
        fence = [[0] * length for _ in range(self.key)]
        row, col = 0, 0
        down = True

        for _ in range(length):
            if row == 0:
                down = True
            elif row == self.key - 1:
                down = False

            fence[row][col] = 1
            col += 1

            if down:
                row += 1
            else:
                row -= 1

        return fence