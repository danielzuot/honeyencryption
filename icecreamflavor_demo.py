# icecreamflavor_demo.py

# demo for basic ice cream flavor honey encryption example

from generic_alphabet import *
from DTE import *

# Define specifications

# alphabet - vanilla, strawberry, mint, chocolate
flavors = ["V", "S", "M", "C"]

# letter probability
flavor_prob = {"C" : .375, "M" : .125,
               "S" : .25, "V" : .25}

# message length
length = 1

# Create probability functions
icecream_fxns = GenericAlphabetProbabilityFxns(flavors, flavor_prob, length)

