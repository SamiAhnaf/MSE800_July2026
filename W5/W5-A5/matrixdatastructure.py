class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def display(self):
        for row in self.data:
            print(row)

    def multiply(self, other):
        # Check whether multiplication is possible
        if self.cols != other.rows:
            raise ValueError(
                "Matrix multiplication is not possible. "
                "Columns of Matrix 1 must equal rows of Matrix 2."
            )

        # Create an empty result matrix
        result = []

        for i in range(self.rows):
            new_row = []

            for j in range(other.cols):
                total = 0

                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]

                new_row.append(total)

            result.append(new_row)

        return Matrix(result)


# ---------------- MAIN PROGRAM ----------------

# Matrix 1: 3 x 5
matrix1_data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Matrix 2: 5 x 2
matrix2_data = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]

# Create Matrix objects
matrix1 = Matrix(matrix1_data)
matrix2 = Matrix(matrix2_data)

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

# Multiply the matrices
try:
    result = matrix1.multiply(matrix2)

    print("\nResult of Matrix 1 x Matrix 2:")
    result.display()

except ValueError as error:
    print(error)