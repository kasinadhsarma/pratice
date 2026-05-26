class addition:
    def add(self,matrix1:list,matrix2:list)->list:
        # get the dimensions of the matrices
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        # check if the matrices can be added
        if rows1 != rows2 or cols1 != cols2:
            return "Matrices cannot be added"
        # create the result matrix
        result = [[0 for _ in range(cols1)] for _ in range(rows1)]
        # add the matrices
        for i in range(rows1):
            for j in range(cols1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = addition().add(matrix1, matrix2)
print(result)