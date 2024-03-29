"""
This is a class for working with Young Tableau

A Young Tableau represents a partition of some natural number, n
Say, n = 8, and the partition is 4, 2, 1, 1
Then the Young diagram is made of 4 rows of 4, 2, 1, and 1 boxes:

    ☐☐☐☐
    ☐☐
    ☐
    ☐

A Young Tableau is a Young diagram with numbers written in the boxes

The partition must be sorted in decreasing order

"""

import warnings
import numpy.polynomial.polynomial as polynomial

# Constants
BOX_CHARACTER = "☐"


class YoungTableau(object):
    def __init__(self, partition: list[int]):
        self.partition = partition
        # Check the partition is valid and warn if not
        if not self.is_valid_partition(partition):
            warnings.warn(f"Invalid partition: {partition}", category=RuntimeWarning)

        self.number_boxes = sum(partition)

    @staticmethod
    def is_valid_partition(partition: list[int]) -> bool:
        """
        A valid partition should be a list of positive integers sorted in decreasing order, with possible repeats
        :param: (list[int]) The partition to check
        :return: (bool) True if the partition is valid, else False
        """
        for value in partition:
            if not isinstance(value, int):  # check its an integer
                raise RuntimeError(f"Invalid partition containing non-integer values: {partition}")
            if value <= 0:  # check its positive
                return False

        # check the list is sorted
        for i in range(0, len(partition) - 1):
            if partition[i] < partition[i + 1]:
                return False

        return True

    def get_diagram_string(self) -> str:
        """
        Print the Young diagram representing the partition
        :return: (str) a string representation of the diagram
        """
        diagram = ""
        for row in self.partition:
            # for each row add the appropriate number of boxes and then start a new line
            diagram += BOX_CHARACTER * row + "\n"

        diagram = diagram[:-1]  # strip trailing newline character
        return diagram

    def __str__(self):
        return self.get_diagram_string()

    def __repr__(self):
        internal_representation = f"Young Tableau with {self.number_boxes} box(es)\n"
        internal_representation += f"Representing the partition {self.partition}\n"
        internal_representation += f"Diagram:\n{self.get_diagram_string()}"
        return internal_representation

    def dimension_polynomial(self):
        """
        Implements the polynomial part of the dimension formula, that is for a diagram, Y, this method
        returns the polynomial f_Y(n) which is such that d_Y = f_Y(n) / hook number
        The polynomial is given by putting n in the top left box, then decreasing to the right,
        then n + 1 in the box below the top left and decreasing to the right and so on
        eg, for the diagram

        ☐☐☐
        ☐☐
        ☐☐
        n   n-1 n-2
        n+1 n
        n+2 n-1

        f_Y(n) = n^2 (n - 2) (n - 1)^2 (n + 1) (n + 2)
        :return: (np.polynomial.polynomial.Polynomial)
        """
        dim_poly = polynomial.Polynomial([1])  # the unit polynomial
        offset = 0
        for row_length in self.partition:
            for i in range(row_length):
                dim_poly *= polynomial.Polynomial([i - offset, 1])  # the polynomial n + offset - i
            offset += 1  # increment starting value each row
        return dim_poly
