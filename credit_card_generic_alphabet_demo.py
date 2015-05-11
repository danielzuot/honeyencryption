# credit_card_generic_alphabet_demo.py

# demo for naive credit card application with generic alphabet

from generic_alphabet import *
from DTE import *

# Define specifications

# alphabet
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# letter probability
number_prob = {"0" : .1, "1" : .1, "2" : .1, "3" : .1, "4" : .1,
               "5" : .1, "6" : .1, "7" : .1, "8" : .1, "9" : .1}

# message length
length = 16

# Create probability functions
cc_fxns = GenericAlphabetProbabilityFxns(numbers, number_prob, length)
