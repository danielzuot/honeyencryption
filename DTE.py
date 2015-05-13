# DTE.py

# Implementation of the distribution transforming encoder (DTE)
# using the API for a message space described in probabilityfunctionAPI.py

import random
import probabilityfunctionAPI

# Define length of seed space
SEED_SPACE_LENGTH = 64
seed_space = 2**SEED_SPACE_LENGTH - 1

"""
Takes in a message and a MessageSpaceProbabilityFxns object
and returns a corresponding random bit string in
the seed space.
"""
def encode(m, pfxns):
    # get range of seed space to pick random string from
    start = pfxns.cumul_distr(m) * seed_space
    end = int(start + pfxns.prob_distr(m)*seed_space) - 1 
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
    if size == 1 or size == 0:
        return table[start]
    
    mid = start + size/2
    (mid_value, mid_msg) = table[mid]
    # recursion step
    if value >= mid_value:
        return binary_search(table, mid, end, value)
    else:
        return binary_search(table, start, mid, value)
    

"""
Takes in a seed and a MessageSpaceProbabilityFxns object and
runs binary search on pre-calculated inverse sampling table and linear
search to find corresponding message.
"""
def decode(s, pfxns):
    table = pfxns.get_inverse_cumul_distr_samples()
    seed_loc = float(s)/seed_space
    (prev_value, prev_msg) = binary_search(table, 0, len(table), seed_loc)
    next_msg = pfxns.next_message(prev_msg)
    next_value = pfxns.cumul_distr(next_msg)
    if next_msg == prev_msg: # at max message
        return prev_msg
    # begin linear scan to find which range seed s falls in
    while seed_loc >= next_value:
        # update prev and next
        (prev_value, prev_msg) = (next_value, next_msg)
        next_msg = pfxns.next_message(prev_msg)
        next_value = pfxns.cumul_distr(next_msg)
    
    return prev_msg
