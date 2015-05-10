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
    return prefix_cumul

"""
Creates list of ordered prefixes
"""
def create_prefix_ordered_list(prefix_prob):
    return sorted(prefix_prob,key = prefix_prob.get)

"""
Create inverse sampling table
"""
def create_inverse_sample_table(prefix_order, prefix_cumul, prefix_lengths):
    table = [] #prob, m
    for prefix in prefix_order:
        #'******'
        cumul_prob = prefix_cumul[prefix]
        num_prefix = prefix.replace('*','0')
        m = str(luhn(int(num_prefix+'0'*(prefix_lengths[prefix]-7))))
        table.append((cumul_prob,m))
    return table

# given random message string as int, return int message with last digit appended such that new string is Luhn-valid
def luhn(m):
    sum = 0
    for i in range(len(str(m))):
        sum += int(i)
    last = 9 * sum % 10
    return m * 10 + last

class CreditCardProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, prefix_prob, prefix_lengths):
        self.prefix_prob = prefix_prob
        self.prefix_lengths = prefix_lengths
        self.prefix_order = create_prefix_ordered_list(prefix_prob)
        self.prefix_cumul = create_cumul_fxn(self.prefix_order, prefix_prob)
        self.inverse_table = create_inverse_sample_table(self.prefix_order, self.prefix_cumul, prefix_lengths)


        # define probability distribution fxn
        def prob(self, m):
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                prefixStr = ''.join(prefix)
                print prefixStr
                if prefixStr in self.prefix_prob:
                    prefixProb = self.prefix_prob[prefixStr]
                    #last digit is the check dig
                    randomDigs = m[6:-1]
                    numRandomDigs = len(randomDigs)
                    print randomDigs
                    print numRandomDigs
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
                    prefixCumul = self.prefix_cumul[prefixStr]
                    totalCumul = prefixCumul + int(randomDigs)*pow(10,-numRandomDigs)
                    return totalCumul
            print "Invalid credit card"
            return -1

        # define next message fxn
        # simplified to never carry over to another prefix
        def next_msg(self,m):
            baseNumber = int(m[:-1])
            return str(luhn(baseNumber+1))

        # create get sample table
        def get_inverse_table(self):
            return self.inverse_table

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxns.__init__(self, cumul, prob, next_msg, get_inverse_table)

    
