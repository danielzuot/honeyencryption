# credit_card.py

# Creation of the proper probability functions required
# (cumul_distr, prob_distr, next_message, get_inverse_cumul_distr_samples)
# to create a MessageSpaceProbabilityFxns object that represents
# the message space of credit cards.

"""
Requires: 

Dictionary of prefix-probabilities {'prefix',prob(prefix)}, where sum of all prob(prefix) = 1
Dictionary of prefix-lengths {'prefix',length}, where length = number of digits in credit cards with prefix 'prefix'

"""

from probabilityfunctionAPI import MessageSpaceProbabilityFxns
import math

"""
Creates prefix cumulative probability distribution
"""
def create_cumul_fxn(prefix_order, prefix_prob):
    cumul_prob = 0
    prefix_cumul = {}
    for prefix in prefix_order:
        prefix_cumul[prefix] = cumul_prob
        cumul_prob += prefix_prob[prefix]
    return 

"""
Creates list of ordered prefixes
"""
def create_prefix_ordered_list(prefix_prob):
    return sorted(prefix_prob,key = prefix_prob.get)

"""
Create inverse sampling table
"""
def create_inverse_sample_table(alphabet, letter_cumul, msg_len):
    return []


class CreditCardProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, prefix_prob, prefix_lengths):
        self.prefix_prob = prefix_prob
        self.prefix_lengths = prefix_lengths
        self.prefix_order = create_prefix_ordered_list(prefix_prob)
        self.prefix_cumul = create_cumul_fxn(self.prefix_order, prefix_prob)
        #self.inverse_table = create_inverse_sample_table(alphabet, self.letter_cumul, msg_len)

        # given random message string, return message with last digit appended such that new string is Luhn-valid
        def luhn(self, m):
            sum = 0
            [sum += int(i) for i in range(len(str(m)))]
            return m * 10 + (9 * sum % 10)

        # define probability distribution fxn
        def prob(self, m):
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                prefixStr = ''.join(prefix)
                if prefixStr in self.prefix_prob:
                    prefixProb = self.prefix_prob[prefixStr]
                    #last digit is the check dig
                    randomDigs = m[6:-1]
                    numRandomDigs = len(randomDigs)
                    prob = prefixProb * math.pow(10,-numRandomDigs)
                    return prob
            print "Invalid credit card"
            return 0

        # define cumul distribution fxn
        def cumul(self, m):
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                prefixStr = ''.join(prefix)
                if prefixStr in self.prefix_prob:
                    #last digit is the check dig
                    randomDigs = m[6:-1]
                    numRandomDigs = len(randomDigs)
                    prefixCumul = prefix_cumul[prefixStr]
                    totalCumul = prefixCumul + int(randomDigs)*pow(10,-numRandomDigs)
                    return totalCumul
            print "Invalid credit card"
            return 0

        # define next message fxn
        # simplified to never carry over to another prefix
        def next_msg(self,m):
            baseNumber = int(m[:-1])
            return luhn(baseNumber+1)

        # create get sample table
        def get_inverse_table(self):
            return self.inverse_table

        # helper function to get denominator of prefix probabilities
        def getTotalProbability(bin):
            sum = 0
            [sum += bin[i][1] for i in bin]
            return sum

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxns.__init__(self, cumul, prob, next_msg, get_inverse_table)

    
