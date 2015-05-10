# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py
# work together.

from credit_card import *
from DTE import *


''' Create prefix_prob and prefix_lengths dictionaries 
i.e. 
prefix_prob = {
    '5235**': 0.0001
    '4*****': 0.1
}
prefix_lengths = {
    '5235**': 16
    '4*****'"" 15
}

'''
prefix_prob = {'414***':0.2, '5*****':0.8}
prefix_lengths = {'414***':8,'5*****':10}




# Create probability fxns
credit_card_fxns = CreditCardProbabilityFxns(prefix_prob,prefix_lengths)
print credit_card_fxns.cumul_distr('41401122')
# Use DTE on random example which is definitely not my actual credit card number
'''seed = encode("4264510252697811", credit_card_fxns)
#print hex(seed)

message = decode(seed, credit_card_fxns)
#print message
'''