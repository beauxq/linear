__author__ = 'Doug'

from fractions import Fraction


class Matrix:
    def __init__(self, num_of_rows, num_of_columns):
        self.row = []
        for i in range(num_of_rows):
            self.row.append([])
            for j in range(num_of_columns):
                self.row[-1].append(None)  # no values in the matrix

    def __repr__(self):
        to_return = ""
        for row in self.row:
            for column in row:
                if column.denominator == 1:
                    to_return += " " + "{:9d}".format(column.numerator)
                else:  # denominator is not 1
                    str_denom = str(column.denominator)
                    str_numer_width = str(9 - (len(str_denom) + 1))  # str of width available for numerator
                    to_return += " " + ("{:" + str_numer_width + "d}").format(column.numerator) + "/" + str_denom

            to_return += "\n"

        return to_return


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
                    to_return.row[i][j] = Fraction(input("coefficient for x" + str(j+1) + "? "))
                except ValueError:
                    to_return.row[i][j] = None
        # right side of equals
        while to_return.row[i][-1] is None:
            try:
                to_return.row[i][-1] = Fraction(input("right side of equals? "))
            except ValueError:
                to_return.row[i][-1] = None

    return to_return


def main():

    matrix = create_matrix()

    print(matrix)


if __name__ == "__main__":
    main()
