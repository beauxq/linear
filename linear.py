__author__ = 'Doug'

class Matrix:
    def __init__(self, num_of_rows, num_of_columns):
        self.row = []
        for i in range(num_of_rows):
            self.row.append([])
            for j in range(num_of_columns):
                self.row[-1].append(None)  # no values in the matrix


def create_matrix():
    # input size
    num_of_rows = 0
    while num_of_rows < 1:
        try:
            num_of_rows = int(input("number of equations? "))
        except ValueError:
            num_of_rows = 0

    num_of_variables = 0
    while num_of_variables < 1:
        try:
            num_of_variables = int(input("number of variables? "))
        except ValueError:
            num_of_variables = 0

    # create empty matrix
    to_return = Matrix(num_of_rows, num_of_variables + 1)  # + 1 for right side of equals

    # fill matrix with values
    for i in range(num_of_rows):
        print("equation ", i+1)
        for j in range(num_of_variables):
            while to_return.row[i][j] is None:
                try:
                    to_return.row[i][j] = int(input("coefficient for x" + str(j+1) + "? "))
                except ValueError:
                    to_return.row[i][j] = None
        # right side of equals
        while to_return.row[i][-1] is None:



def main():

    matrix = create_matrix()
