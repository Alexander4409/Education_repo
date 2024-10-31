word = ['у', 'н', 'и', 'к', 'у', 'м']
wight, height = 5, 7
matrix = [[" " for i in range(wight)] for j in range(height)]
matrix2 = [[" " for i in range(wight)] for j in range(height)]
pos = 3
pos1 = 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 and (j == 1 or j == 2 or j == 3):
            matrix[i][j] = "*"
        elif (i == 1 and (j == 0 or j == 4)) or (i == 2 and j == 4):
            matrix[i][j] = "*"
        elif i > 2:
            if j == pos:
                matrix[i][j] = "*"
                pos -= 1
            if i == 3:
                matrix[i][0:3] = word[3:]

for p in range(len(matrix2)):
    for q in range(len(matrix2[p])):
        if p == 0 and (q == 1 or q == 2 or q == 3):
            matrix2[p][q] = "*"
        elif (p == 1 and (q == 0 or q == 4)) or (p == 2 and q == 0):
            matrix2[p][q] = "*"
        elif p > 2:
            if q == pos1:
                matrix2[p][q] = "*"
                pos1 += 1
                p += 1
            elif p == 3:
                matrix2[p][q+2] = "у"
                matrix2[p][q+3] = "н"
                matrix2[p][q+4] = "и"

final_matrix = []

for a, b in zip(matrix2, matrix):
    final_matrix.append(a+b)

for row in final_matrix:
    for _ in row:
        print(_, end='\t')
    print()