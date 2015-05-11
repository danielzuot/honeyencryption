# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py
# work together.

from credit_card import *
from DTE import *


''' Create prefixes dictionary 'prefix': [numRandom, cardLength, probWeight]
i.e. 
prefixes = {
    '5235**': [2, 8, 1],
    '123456': [5, 8, 1]
}

'''

prefixes = {
    '5235**': [2, 8, 100],
    '123456': [0, 8, 1]
}

#with open('bin.txt','r') as bin:
#    prefixes = eval(bin.read())



# Create probability fxns
credit_card_fxns = CreditCardProbabilityFxns(prefixes)
print credit_card_fxns.next_message('52350070')
# Use DTE on random example which is definitely not my actual credit card number
'''seed = encode("4264510252697811", credit_card_fxns)
#print hex(seed)

message = decode(seed, credit_card_fxns)
#print message
'''