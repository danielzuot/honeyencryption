# DTE.py

# Implementation of the distribution transforming encoder (DTE)
# using the API for a message space described in probabilityfunctionAPI.py

import random

# Define length of seed space
SEED_SPACE_LENGTH = 128
seed_space = 2**SEED_SPACE_LENGTH - 1

"""
Takes in a message and returns a corresponding random bit string in
the seed space.
"""
def encode(m):
    # get range of seed space to pick random string from
    start = cumul_distr(m) * seed_space
    end = int(start + prob_distr(m)*seed_space) - 1 
    start = int(start)

    # pick random string from corresponding seed space
    seed = int(random.random() * (end-start) + start)
    
    return seed

"""
Takes in an ordered table [(value, msg)] and a value to search for in the table.
Returns the highest index message in the table that is less than the inputted value.
Initial call : binary_search(table, 0, len(table), value)
"""
def binary_search(table, start, end, value):
    size = end - start
    # base case
    if size == 1:
        return table[start]
    
    mid = start + size/2
    (mid_value, mid_msg) = table[mid]
    # recursion step
    if value > mid_value:
        return binary_search(table, mid, end, value)
    else:
        return binary_search(table, start, mid+1, value)
    

"""
Runs binary search on pre-calculated inverse sampling table and linear
search to find corresponding message.
"""
def decode(s, table):
    (prev_value, prev_msg) = binary_search(table, 0, len(table), s)
    next_msg = next_message(prev_msg)
    next_value = cumul_distr(next_msg)
    # begin linear scan to find which range seed s falls in
    while s >= next_value:
        # update prev and next
        (prev_value, prev_msg) = (next_value, next_msg)
        next_msg = next_message(prev_msg)
        next_value = cumul_distr(next_msg)
    
    return prev_msg
