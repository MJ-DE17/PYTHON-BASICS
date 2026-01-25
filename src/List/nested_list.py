matrix = [[1,2,3],[4,5,6]]

def mat(matrix):
    for row in matrix :
        for val in row:
            print(val)

mat(matrix)

# Flatten Using List Comprehension
flat = [ val for row in matrix for val in row ]
print(flat)

# sum
def sumy(a):
    total = 0
    for row in matrix:
        for val in row :
            total += val
    return total
print(sumy(matrix))

print("----")
# sum of each row
def sumyr(a):
    total = 0
    for row in matrix:
        print(sum(row))
sumyr(matrix)

def colsum(a):
    for col in range(len(matrix[0])):
        col_sum = 0
        for row in range(len(matrix)):
            col_sum += matrix[row][col]
        print(col_sum)

matrix = [[1, 9], [3, 4]]
max_val = matrix[0][0]

for row in matrix:
    for val in row:
        if val > max_val:
            max_val = val

print(max_val)

