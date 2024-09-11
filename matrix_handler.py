class matrix():
        def __init__(self, data=[]):
                self.data = data

        def dot_product(self, a, b):
                els = len(a)
                if els != len(b):
                        return False

                return sum([a[i]*b[i] for i in range(els)])

        def get_col(self, num):
                col = []
                for row in self.data:
                        col.append(row[num])
                return col

        def __mul__(self, other):
                output_matrix = [[0 for x in range(len(other.data[0]))] for x in range(len(self.data))]
                for i,row in enumerate(self.data):
                        for j in range(len(other.data[0])):
                                output_matrix[i][j] = self.dot_product(other.get_col(j), row)

                return matrix(output_matrix)


        def __str__(self):
                return "\n".join([" ".join([str(el) for el in row]) for row in self.data])

#Examples
mymat = matrix([[1,2,3],[4,5,6]])
mymat2 = matrix([[7,8],[9,10],[11,12]])
print(mymat * mymat2)
