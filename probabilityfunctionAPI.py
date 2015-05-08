# probabilityfunctionAPI.py

# This file describes the API required to build the probability functions
# used by the Distribution Transforming Encoder (DTE) for a message space




"""
The cumulative probability distribution function for the ordered message
space. Takes in a string for the message and returns a probability value
between <= 1 and > 0 representing where in the ordered probability space
that message lies.
"""
def cumul_distr(message):
    return

"""
The probability distribution function for the ordered message space. Takes
in a string for the message and returns a probability value between <= 1
and > 0 representing the probability of that single message.
"""
def prob_distr(message):
    return

"""
Given an input message, return the next message in the ordered message space.
"""
def next_message(message):
    return

"""
List of pre-calculated sampling of cumulative distribution values to messages.
The samples will be evenly spaced and the number of samples will be determined
by the size of the message space. It will be used for binary search on the
probability values during decoding. ([value, msg])
"""
def get_inverse_cumul_distr_samples():
    return []

"""
Class used to bundle all the above functions into one object for easy access.
"""
class MessageSpaceProbabilityFxns:
    """
    Creator method takes in specified functions.
    """
    def __init__(self, cumul, prob, next_msg, inverse_samples):
        self.cumul = cumul
        self.prob = prob
        self.next_msg = next_msg
        self.inverse_samples = inverse_samples
        
    def cumul_distr(self, m):
        return self.cumul(self, m)
    def prob_distr(self, m):
        return self.prob(self, m)
    def next_message(self, m):
        return self.next_msg(self, m)
    def get_inverse_cumul_distr_samples(self):
        return self.inverse_samples(self)
    
        
