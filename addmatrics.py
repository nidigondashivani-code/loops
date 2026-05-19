A = [
    [2, 21, 3],
    [7, 5, 6],
    [9, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 15, 41],
    [7, 21, 12]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(A)):          # rows
    for j in range(len(A[0])):   # columns
        result[i][j] = A[i][j] + B[i][j]

print("Resultant Matrix:")
for row in result:
    print(row)