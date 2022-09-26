"""
Unit tests for the YoungTableau class
"""

import YoungTableau
import numpy.polynomial.polynomial as polynomial
import unittest


class TestYoungTableau(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_diagram(self):
        young_tableau = YoungTableau.YoungTableau([4, 2, 1, 1])
        expected_diagram = "☐☐☐☐\n☐☐\n☐\n☐"
        self.assertEqual(young_tableau.get_diagram_string(), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([7, 4, 3, 3, 2, 1])
        expected_diagram = "☐☐☐☐☐☐☐\n☐☐☐☐\n☐☐☐\n☐☐☐\n☐☐\n☐"
        self.assertEqual(young_tableau.get_diagram_string(), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([1, 1, 1, 1, 1])
        expected_diagram = "☐\n☐\n☐\n☐\n☐"
        self.assertEqual(young_tableau.get_diagram_string(), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([5])
        expected_diagram = "☐☐☐☐☐"
        self.assertEqual(young_tableau.get_diagram_string(), expected_diagram)

    def test_str(self):
        young_tableau = YoungTableau.YoungTableau([4, 2, 1, 1])
        expected_diagram = "☐☐☐☐\n☐☐\n☐\n☐"
        self.assertEqual(str(young_tableau), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([7, 4, 3, 3, 2, 1])
        expected_diagram = "☐☐☐☐☐☐☐\n☐☐☐☐\n☐☐☐\n☐☐☐\n☐☐\n☐"
        self.assertEqual(str(young_tableau), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([1, 1, 1, 1, 1])
        expected_diagram = "☐\n☐\n☐\n☐\n☐"
        self.assertEqual(str(young_tableau), expected_diagram)

        young_tableau = YoungTableau.YoungTableau([5])
        expected_diagram = "☐☐☐☐☐"
        self.assertEqual(str(young_tableau), expected_diagram)

    def test_repr(self):
        partition = [4, 2, 1, 1]
        number_boxes = 8
        young_tableau = YoungTableau.YoungTableau(partition)
        expected_representation = f"Young Tableau with {number_boxes} box(es)\n"
        expected_representation += f"Representing the partition {partition}\n"
        expected_diagram = "☐☐☐☐\n☐☐\n☐\n☐"
        expected_representation += f"Diagram:\n{expected_diagram}"
        self.assertEqual(repr(young_tableau), expected_representation)

        partition = [7, 4, 3, 3, 2, 1]
        number_boxes = 20
        young_tableau = YoungTableau.YoungTableau(partition)
        expected_representation = f"Young Tableau with {number_boxes} box(es)\n"
        expected_representation += f"Representing the partition {partition}\n"
        expected_diagram = "☐☐☐☐☐☐☐\n☐☐☐☐\n☐☐☐\n☐☐☐\n☐☐\n☐"
        expected_representation += f"Diagram:\n{expected_diagram}"
        self.assertEqual(repr(young_tableau), expected_representation)

        partition = [1, 1, 1, 1, 1]
        number_boxes = 5
        young_tableau = YoungTableau.YoungTableau(partition)
        expected_representation = f"Young Tableau with {number_boxes} box(es)\n"
        expected_representation += f"Representing the partition {partition}\n"
        expected_diagram = "☐\n☐\n☐\n☐\n☐"
        expected_representation += f"Diagram:\n{expected_diagram}"
        self.assertEqual(repr(young_tableau), expected_representation)

        partition = [5]
        number_boxes = 5
        young_tableau = YoungTableau.YoungTableau(partition)
        expected_representation = f"Young Tableau with {number_boxes} box(es)\n"
        expected_representation += f"Representing the partition {partition}\n"
        expected_diagram = "☐☐☐☐☐"
        expected_representation += f"Diagram:\n{expected_diagram}"
        self.assertEqual(repr(young_tableau), expected_representation)

    def test_is_valid_partition(self):
        young_tableau = YoungTableau.YoungTableau([1])  # the partition doesn't matter in this test
        # Valid partitions
        self.assertTrue(young_tableau.is_valid_partition([4, 2, 1, 1]))
        self.assertTrue(young_tableau.is_valid_partition([7, 4, 3, 3, 2, 1]))
        self.assertTrue(young_tableau.is_valid_partition([1, 1, 1, 1, 1]))
        self.assertTrue(young_tableau.is_valid_partition([5]))

        # Invalid partitions
        self.assertFalse(young_tableau.is_valid_partition([7, 8, 3, 3, 2, 1]))
        self.assertFalse(young_tableau.is_valid_partition([1, 1, 1, 1, -1]))
        self.assertFalse(young_tableau.is_valid_partition([3, 2, 1, 4]))

    def test_invalid_partition_warning(self):
        with self.assertWarns(RuntimeWarning):
            YoungTableau.YoungTableau([7, 8, 3, 3, 2, 1])
        with self.assertWarns(RuntimeWarning):
            YoungTableau.YoungTableau([1, 1, 1, 1, -1])
        with self.assertWarns(RuntimeWarning):
            YoungTableau.YoungTableau([3, 2, 1, 4])

    def test_dimension_polynomial(self):
        # ☐☐
        # ☐☐
        young_tableau = YoungTableau.YoungTableau([2, 2])
        # should be n^2(n^2 - 1) = n^4 - n^2
        self.assertEqual(young_tableau.dimension_polynomial(), polynomial.Polynomial([0, 0, -1, 0, 1]))
        # ☐
        # ☐
        # ☐
        # ☐
        young_tableau = YoungTableau.YoungTableau([1, 1, 1, 1])
        # should be n(n - 1)(n - 2)(n - 3) = -6 n + 11 n^2 - 6 n^3 + n^4
        self.assertEqual(young_tableau.dimension_polynomial(), polynomial.Polynomial([0, -6, 11, -6, 1]))
        # ☐☐☐☐
        young_tableau = YoungTableau.YoungTableau([4])
        # should be n(n + 1)(n + 2)(n + 3) = 6 n + 11 n^2 + 6 n^3 + n^4
        self.assertEqual(young_tableau.dimension_polynomial(), polynomial.Polynomial([0, 6, 11, 6, 1]))
        # ☐☐☐☐
        # ☐☐
        # ☐
        # ☐
        young_tableau = YoungTableau.YoungTableau([4, 2, 1, 1])
        # should be n^2(n + 1)(n + 2)(n + 3)(n - 1)(n - 2)(n - 3) = -36 n^2 + 49 n^4 - 14 n^6 + n^8
        self.assertEqual(young_tableau.dimension_polynomial(), polynomial.Polynomial([0, 0, -36, 0, 49, 0, -14, 0, 1]))

if __name__ == "__main__":
    unittest.main()
