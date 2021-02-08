mat_1 = [[4, 8, 5, 2], [7, 1, 4, 9], [2, 6, 8, 1]]
mat_2 = [[3, 0, 7, 4], [1, 8, 5, 2], [9, 6, 7, 4]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return ", ".join(" ".join([str(val) for val in line]) for line in self.lists)

    def __add__(self, other):
        mat_3 = []
        for i in range(len(self.lists)):
            mat_3.append([])
            for v in range(len(self.lists[0])):
                mat_3[i].append(self.lists[i][v] + other.lists[i][v])
        return ", ".join(map(str, mat_3))


matrix_1 = Matrix(mat_1)
matrix_2 = Matrix(mat_2)
print(f"'Матрица 1:' {matrix_1}")
print(f"'Матрица 2:' {matrix_2}")
print(f"'Матрица 1 + Матрица 2:' {matrix_1 + matrix_2}")
