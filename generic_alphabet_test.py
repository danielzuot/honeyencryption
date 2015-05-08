# generic_alphabet_test.py

# Tests to see if the methods in generic_alphabet.py, probabilityfunctionAPI.py, and DTE.py
# work together with a basic example.

from generic_alphabet import *
from DTE import *


# ALPHA-10 - 10 letter alphabet
alpha_10 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
alpha_10_prob = {"a" : .05, "b" : .05, "c" : .4, "d" : .01, "e" : .09,
                 "f" : .07, "g" : .03, "h" : .05, "i" : .05, "j" : .2 }
alpha_10_msg_len = 4

# Create probability fxns
alpha_10_fxns = GenericAlphabetProbabilityFxns(alpha_10, alpha_10_prob, alpha_10_msg_len)

# Use DTE on examples
seed = encode("aabb", alpha_10_fxns)
print hex(seed)

message = decode(seed, alpha_10_fxns)
print message
