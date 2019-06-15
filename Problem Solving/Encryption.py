'''

Problem: Given an input string, encrypt it by specified scheme.
URL: https://www.hackerrank.com/challenges/encryption/

Runtime: O(n)
'''


import math as mt

def encrypt(s):
    rows = 0
    cols = 0
    square_root = mt.sqrt(len(s))

    if square_root % 2 == 0:
        rows = int(square_root)
        cols = int(square_root)
    else:
        rows = int(mt.floor(square_root))
        cols = int(mt.ceil(square_root))

    while (rows * cols) < len(s):
        rows += 1

    #print("{} x {}".format(rows, cols))


    i = 0
    matrix = []
    for _ in range(0, rows):
        row = []
        for _ in range(0, cols):
            if i < len(s):
                row.append(s[i])
            else:
                row.append("#")
            i += 1
        matrix.append(row)

    #print(matrix)

    output = []
    for index in range(len(matrix[0])):
        output_row = [row[index] for row in matrix if row[index] != "#"]
        output.append("".join(output_row))
    return " ".join(output)


if __name__ == '__main__':
    text = "iffactsdontfittotheorychangethefacts"
    encrypt(text)