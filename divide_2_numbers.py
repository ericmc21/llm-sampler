
def divide_numbers(numerator, denominator):
    """
    Divide two numbers and return the result.

    This function takes two numbers as input and returns the result of dividing
    the numerator by the denominator. It handles division by zero and type errors
    gracefully, returning error messages instead of raising exceptions.

    Parameters:
    numerator (int or float): The number to be divided (the dividend).
    denominator (int or float): The number by which to divide (the divisor).

    Returns:
    float: The result of the division if both inputs are valid numbers and the 
           denominator is not zero.
    str: An error message if division by zero is attempted or if the inputs are not numbers.

    Examples:
    >>> divide_numbers(10, 2)
    5.0

    >>> divide_numbers(10, 0)
    'Error: Division by zero is not allowed.'

    >>> divide_numbers(10, 'a')
    'Error: Both inputs must be numbers.'

    Edge Cases:
    - If the denominator is zero, the function returns an error message.
    - If either the numerator or denominator is not of type int or float, the function
      returns an error message.
    - If both numerator and denominator are zero, the function will return a division by
      zero error.

    """

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."

# Example usage
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: Division by zero is not allowed.
print(divide_numbers(10, 'a'))  # Output: Error: Both inputs must be numbers.


import unittest

class TestDivideNumbers(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(divide_numbers(10, 2), 5.0)
        self.assertEqual(divide_numbers(9, 3), 3.0)
        self.assertEqual(divide_numbers(-10, 2), -5.0)
        self.assertEqual(divide_numbers(10, -2), -5.0)
        self.assertEqual(divide_numbers(-10, -2), 5.0)
        self.assertAlmostEqual(divide_numbers(1, 3), 0.3333333333333333)

    def test_edge_cases(self):
        self.assertEqual(divide_numbers(0, 1), 0.0)
        self.assertEqual(divide_numbers(0, -1), 0.0)
        self.assertEqual(divide_numbers(1, 0), "Error: Division by zero is not allowed.")
        self.assertEqual(divide_numbers(0, 0), "Error: Division by zero is not allowed.")
        
    def test_type_error_cases(self):
        self.assertEqual(divide_numbers(10, 'a'), "Error: Both inputs must be numbers.")
        self.assertEqual(divide_numbers('a', 10), "Error: Both inputs must be numbers.")
        self.assertEqual(divide_numbers('a', 'b'), "Error: Both inputs must be numbers.")
        self.assertEqual(divide_numbers(10, None), "Error: Both inputs must be numbers.")
        self.assertEqual(divide_numbers(None, 10), "Error: Both inputs must be numbers.")

    def test_floating_point_division(self):
        self.assertEqual(divide_numbers(5.5, 2.2), 2.5)
        self.assertEqual(divide_numbers(-5.5, 2.2), -2.5)
        self.assertEqual(divide_numbers(5.5, -2.2), -2.5)
        self.assertEqual(divide_numbers(-5.5, -2.2), 2.5)


if __name__ == '__main__':
    unittest.main()