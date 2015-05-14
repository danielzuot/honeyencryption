# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py
# work together.

from credit_card import *
from DTE import *
import os
from random import randint

''' Create prefixes dictionary 'prefix': [numRandom, cardLength, probWeight]
i.e. 
prefixes = {
    '5235**': [2, 8, 100],
    '123456': [0, 8, 1]
}
'''
with open('bin.txt','r') as bin:
    prefixes = eval(bin.read())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

credit_card_example = '4117700001669792'
secret_key = 2048101736616812280
#guess_key =  2048101736616812280
guess_key =  3496328831800304765

# Create probability fxns
credit_card_fxns = CreditCardProbabilityFxns(prefixes)


# Use DTE on credit card example
seed = encode(credit_card_example, credit_card_fxns)
ciphertext = secret_key ^ seed
decipher_seed = guess_key ^ ciphertext


print "CREDIT CARD: "+credit_card_example
print ""
print "HEX(SEED): "+str(hex(seed))
print "CIPHERTEXT: "+str(ciphertext)
print "HEX(GUESSED_SEED): "+str(hex(decipher_seed))
print ""

message = decode(decipher_seed, credit_card_fxns)
print "MESSAGE: "+message
