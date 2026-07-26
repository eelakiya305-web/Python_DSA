matrix = []

print("Enter 3x3 matrix")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

magic_sum = sum(matrix[0])

if (sum(matrix[1]) == magic_sum and
    sum(matrix[2]) == magic_sum and
    matrix[0][0] + matrix[1][0] + matrix[2][0] == magic_sum and
    matrix[0][1] + matrix[1][1] + matrix[2][1] == magic_sum and
    matrix[0][2] + matrix[1][2] + matrix[2][2] == magic_sum and
    matrix[0][0] + matrix[1][1] + matrix[2][2] == magic_sum and
    matrix[0][2] + matrix[1][1] + matrix[2][0] == magic_sum):
    print("Magic Square")
else:
    print("Not a Magic Square")
    