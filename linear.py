__author__ = 'Doug Hoskisson'

from fractions import Fraction
from copy import deepcopy


class Matrix:
    def __init__(self, num_of_rows, num_of_columns):
        self.row = []
        for i in range(num_of_rows):
            self.row.append([])
            for j in range(num_of_columns):
                self.row[-1].append(None)  # None is a flag for create_matrix function

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
            num_of_rows = int(input("number of rows? "))
        except ValueError:
            num_of_rows = 0

    num_of_columns = 0
    while num_of_columns < 1:
        try:
            num_of_columns = int(input("number of columns? "))
        except ValueError:
            num_of_columns = 0

    # create empty matrix
    to_return = Matrix(num_of_rows, num_of_columns)  # + 1 for right side of equals

    # fill matrix with values
    for i in range(num_of_rows):
        print("row ", i+1)
        for j in range(num_of_columns):
            while to_return.row[i][j] is None:
                try:
                    to_return.row[i][j] = Fraction(input("column " + str(j+1) + "? "))
                except ValueError:
                    to_return.row[i][j] = None

    return to_return


def index_of_first_nonzero(matrix, row_index):
    """:returns -1 if there are no nonzeros"""
    to_return = 0
    while not matrix.row[row_index][to_return]:  # while is zero
        to_return += 1
        if to_return == len(matrix.row):  # whole row is zero
            return -1
    return to_return


def main():

    matrix_history = []
    matrix = create_matrix()
    matrix_history.append(deepcopy(matrix))

    # TODO add E echelon form, F rref
    menu_text = "R Replacement\nI Interchange\nS Scaling\nQ Quit (display operations)\nWhich operation? "
    valid_input = ["R", "I", "S", "Q"]  # last item should be quit

    operation = "N"
    while operation != valid_input[-1]:  # operations loop, last item in valid_input should be quit
        print(matrix)
        while operation not in valid_input:  # valid input loop
            operation = input(menu_text).upper()
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

            # suggested scalar = (0 - first_nonzero_entry_in_replaced_row) / first_nonzero_entry_in_added_row
            # (if they're in the same column)
            suggested_scalar = 0
            first_index = index_of_first_nonzero(matrix, which_row-1)
            second_index = index_of_first_nonzero(matrix, other_row-1)
            max_index = max(first_index, second_index)
            if (second_index > -1) and (first_index > -1):
                suggested_scalar = Fraction(0 - matrix.row[which_row-1][max_index]) / \
                                   matrix.row[other_row-1][max_index]

            scalar = 0
            if suggested_scalar == 0:
                while scalar == 0:  # valid input loop
                    try:
                        scalar = Fraction(input("With what scalar? "))
                    except ValueError:
                        scalar = 0
            else:  # suggested_scalar != 0
                input_text = "With what scalar? (Enter for " + str(suggested_scalar.numerator) + \
                             (("/" + str(suggested_scalar.denominator))
                              if suggested_scalar.denominator != 1 else "") + ") "
                while scalar == 0:  # valid input loop
                    scalar_input = input(input_text)
                    if scalar_input == "":
                        scalar = suggested_scalar
                    else:  # didn't just press enter
                        try:
                            scalar = Fraction(scalar_input)
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
        if operation != valid_input[-1]:
            matrix_history.append(deepcopy(matrix))
            operation = "N"

    # end operations
    # print history
    for entry in matrix_history:
        print(entry)

if __name__ == "__main__":
    main()
