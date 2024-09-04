from typing import *

from typing import List

# Function with typing to accept a list of integers
def sum_of_lists(x: List[int]):
    print(sum(x))

# Example usage
sum_of_lists([1, 2, 3, 4])  # Output: 10
sum_of_lists([100, 200])    # Output: 300




# Function with typing to accept a list of any type
def sum_of_lists(x: List):
    pass  # This would be the function to accept a list of any type (not used in this example)

# Function with typing to accept a list of integers
def sum_of_lists(x: List[int]):
    print(sum(x))

# Uncommented function definition, accepting any type of input (not used in this example)
# def sum_of_lists(x):
#     print(sum(x))

# Example usage
sum_of_lists([1, 2, 3, 4], "shubham")
sum_of_lists([1, 2, 3, 4])
sum_of_lists([100, 200])
















