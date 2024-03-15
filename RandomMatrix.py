import random

rows = int(input("Enter amount of rows: "))
cols = int(input("Enter amount of cols: "))
col_index = int(input("Enter col index: "))
row_index = int(input("Enter row index: "))

def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 100))
        matrix.append(row)    
    return matrix

def get_column_sum(matrix, col_index):
    col_sum = 0
    for row in matrix:
        if col_index < len(row):
            col_sum += row[col_index]
    return col_sum

def get_row_average(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        return None 

    row_sum = sum(matrix[row_index])
    row_average = row_sum / len(matrix[row_index])
    return row_average



matrix1 = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix1:
    print(row)

col_sum = get_column_sum(matrix1, col_index)
print(f"Sum of column {col_index}: {col_sum}")

row_average = get_row_average(matrix1, row_index)
if row_average is not None:
    print(f"Average of row {row_index}: {row_average}")
else:
    print("Invalid row index")