# algorithms/railfence.py

def encrypt(plaintext, key):
    if key <= 1:
        return plaintext  # if key is 1 or less, return the original text

    rail_matrix = [['' for _ in range(len(plaintext))] for _ in range(key)]
    row = 0
    direction = True  # True = moving down, False = moving up

    for col in range(len(plaintext)):
        rail_matrix[row][col] = plaintext[col]  # place the character in the correct row

        # change direction at the top or bottom row
        if row == 0:
            direction = True
        elif row == key - 1:
            direction = False

        # move to the next row based on the current direction
        if direction:
            row += 1
        else:
            row -= 1

    # read the matrix row by row to get the encrypted text
    cipher_text = ''.join(char for r in rail_matrix for char in r if char)
    return cipher_text


def decrypt(ciphertext, key):
    if key <= 1:
        return ciphertext  # if key is 1 or less, return the original text

    rail_matrix = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    row = 0
    direction = True  # True = moving down, False = moving up

    # mark the positions of characters in the matrix
    for col in range(len(ciphertext)):
        rail_matrix[row][col] = '*'  # placeholder

        if row == 0:
            direction = True
        elif row == key - 1:
            direction = False

        if direction:
            row += 1
        else:
            row -= 1

    # fill the matrix with the characters from the ciphertext
    index = 0
    for r in range(key):
        for c in range(len(ciphertext)):
            if rail_matrix[r][c] == '*' and index < len(ciphertext):
                rail_matrix[r][c] = ciphertext[index]
                index += 1

    # read the plaintext following the zigzag path
    plaintext = []
    row = 0
    direction = True
    for col in range(len(ciphertext)):
        plaintext.append(rail_matrix[row][col])

        if row == 0:
            direction = True
        elif row == key - 1:
            direction = False

        if direction:
            row += 1
        else:
            row -= 1

    return ''.join(plaintext)
