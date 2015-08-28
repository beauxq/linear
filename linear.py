__author__ = 'Doug'

from fractions import Fraction
from copy import deepcopy


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

    matrix_history = []
    matrix = create_matrix()
    matrix_history.append(deepcopy(matrix))

    operation = "N"
    while operation != "E":  # operations loop
        print(matrix)
        while operation not in ["R", "I", "S", "E"]:  # valid input loop
            operation = input("R Replacement\nI Interchange\nS Scaling\nE End\nWhich operation? ")
        if operation == "R":
            # replacement
            which_row = 0
            while which_row < 1 or which_row > len(matrix.row):  # valid input loop
                try:
                    which_row = int(input("Which row to replace? "))
                except ValueError:
                    which_row = 0
            other_row = 0
            while other_row < 1 or other_row > len(matrix.row):  # valid input loop
                try:
                    other_row = int(input("Which row to add? "))
                except ValueError:
                    other_row = 0
            scalar = 0
            while scalar == 0:  # valid input loop
                try:
                    scalar = Fraction(input("With what scalar? "))
                except ValueError:
                    scalar = 0

            for index in range(len(matrix.row[which_row - 1])):
                matrix.row[which_row - 1][index] += matrix.row[other_row - 1][index] * scalar

            dependent_str = ("/" + str(scalar.denominator)) if scalar.denominator != 1 else ""
            matrix_history.append(operation + " (" + str(which_row) + ") + (" + str(other_row) + ") * " +
                                  str(scalar.numerator) + dependent_str)

        elif operation == "I":
            # interchange
            which_row = 0
            while which_row < 1 or which_row > len(matrix.row):  # valid input loop
                try:
                    which_row = int(input("Which row? "))
                except ValueError:
                    which_row = 0
            other_row = 0
            while other_row < 1 or other_row > len(matrix.row):  # valid input loop
                try:
                    other_row = int(input("Which other row? "))
                except ValueError:
                    other_row = 0

            temp_row = deepcopy(matrix.row[which_row - 1])
            matrix.row[which_row - 1] = deepcopy(matrix.row[other_row - 1])
            matrix.row[other_row - 1] = deepcopy(temp_row)

            matrix_history.append(operation + " (" + str(which_row) + ") (" + str(other_row) + ")")

        elif operation == "S":
            # scaling
            which_row = 0
            while which_row < 1 or which_row > len(matrix.row):  # valid input loop
                try:
                    which_row = int(input("Which row? "))
                except ValueError:
                    which_row = 0
            scalar = 0
            while scalar == 0:  # valid input loop
                try:
                    scalar = Fraction(input("Scalar? "))
                except ValueError:
                    scalar = 0

            for index in range(len(matrix.row[which_row - 1])):
                matrix.row[which_row - 1][index] *= scalar

            dependent_str = ("/" + str(scalar.denominator)) if scalar.denominator != 1 else ""
            matrix_history.append(operation + " (" + str(which_row) + ") * " + str(scalar.numerator) + dependent_str)

        # done with operation
        if operation != "E":
            matrix_history.append(deepcopy(matrix))
            operation = "N"

    # end operations
    # print history
    for entry in matrix_history:
        print(entry)

if __name__ == "__main__":
    main()
