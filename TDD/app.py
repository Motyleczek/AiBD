import numpy as np
from typing import List

# function should change any 3x3 square into a magic square, calculate the MINIMUM cost of said change
# cost of one change: abs(a - b) where a is the previous number and b is the new number
# sum of all costs is the total cost

# idea from: https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

def magic_square(square: List[List]) -> int:
    
    # transforming list into ndarray, for ease of operations
    np_square = np.array(square)
    
    # for a 3x3 magic square this is the value that all the columns/rows have to sum up to 
    magic_constant = 15
    
    # checking sum in rows
    np_sum_axis0 = np.sum(np_square, axis=0)
    axis0_magic = np.all(np_sum_axis0 == magic_constant)
    
    # checking sum in columns
    np_sum_axis1 = np.sum(np_square, axis=1)
    axis1_magic = np.all(np_sum_axis1 == magic_constant)
    
    # below the minimal cost is calculated the same way for both columns/rows
    cost = 0
    if not axis1_magic:
        # we check the sum of all columns
        sum_axis = np.sum(np_sum_axis1)
        diff = np.abs(sum_axis - 3*magic_constant)
        
        # if its 45 it means that there are correct numbers in the array, but in wrong order. 
        if diff == 0:
            # calculation of cost
            max_val = np.max(np_sum_axis1)
            cost = (max_val - magic_constant) * 2
            return cost
        
        # else it means that the numbers are wrong - it does not matter what those numbers are,
        # the cost will always be the same
        else:
            cost = diff
    
    # same idea with second 'sum'
    if not axis0_magic:
        sum_axis = np.sum(np_sum_axis0)
        diff = np.abs(sum_axis - 3*magic_constant)
        if diff == 0:
            max_val = np.max(np_sum_axis0)
            cost = (max_val - magic_constant) * 2
            return cost
        
        else:
            cost = diff
    
    # if not, it is indeed a magic square -> cost is equal to 0
    return cost