
class Matrix:

    def __init__(self, rows, colums):
        self.rows_num = rows
        self.colums_num = colums
        matrix = []
        while len(matrix) < colums:
            matrix_colum = []
            while len(matrix_colum) < rows:
                matrix_colum.append(int(input(f'Заполните {len(matrix)+1} столбец из {rows} элементов, введите элемент {len(matrix_colum)+1}: ')))
            matrix.append(matrix_colum)
        self.matrix = matrix
        print(matrix)

    def __str__(self):
        for i in range(self.rows_num):
            row = []
            for b in range(self.colums_num):
                row.append(self.matrix[b][i])
            print(f'   *{row}*')
        return f'Матрица {self.rows_num} на {self.colums_num}'

    def __add__(self, other):
        if self.rows_num != other.rows_num or self.colums_num != self.colums_num: #и вот это не выполнелось
            print(f'Для сложения матрицы должны иметь одну размерность')
            raise ValueError
        matrix_sum = []
        row_counter = 0
        while len(matrix_sum) < self.colums_num:
            matrix_sum_colum = []
            colum_counter = 0
            while len(matrix_sum_colum) < self.rows_num:
                matrix_sum_colum.append(self.matrix[row_counter][colum_counter] + other.matrix[row_counter][colum_counter])
                colum_counter += 1
            matrix_sum.append(matrix_sum_colum)
            row_counter += 1
        return matrix_sum

matrix_1 = Matrix(2,3)
matrix_2 = Matrix(2,3)
print(matrix_1)
print(matrix_2)

b = matrix_1 + matrix_2
print(b)
print(type(b)) # Не пойму почету при суммировании объектов класса Матрица, на выходе получаем объект класса Лист

# 2 задание

class Clothes:
    def __init__(self):
        pass
        #total_cloth = []
        #self.total_cloth = total_cloth
    total_cloth = []

class Coat(Clothes):
    def __init__(self, size):
        #super(Clothes).__init__()
        self.size = size
        self.am_cloth = self.size / 6.5 + 0.5
        Clothes.total_cloth.append(self.am_cloth)

    @property
    def coat_cloth_am(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, size):
        self.size = size
        self.am_cloth = self.size * 2 + 0.3
        Clothes.total_cloth.append(self.am_cloth)

    @property
    def suit_cloth_am(self):
        return self.size * 2 + 0.3

coat_1 = Coat(87)
suit_1 = Suit(56)

print(f' Общий расход ткани: {sum(coat_1.total_cloth)}')
print(coat_1.coat_cloth_am)
print(suit_1.suit_cloth_am)

# 3 задание

class Cell:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return self.elements + other.elements

    def __sub__(self, other):
        return self.elements - other.elements

    def __mul__(self, other):
        return self.elements * other.elements

    def __truediv__(self, other):
        return self.elements // other.elements

    def make_order(self, row_el):
        self.row_el = row_el
        self.colums = self.elements // self.row_el
        counter = 0
        while counter < self.colums:
            print('*' * row_el, '\n')
            counter +=1

        print('*' * int(self.elements % self.row_el))

cell_1 = Cell(15)
cell_2 = Cell(17)

cell_1.make_order(5)
cell_2.make_order(5)
