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

# helper function to get denominator of prefix probabilities
def getTotalProbability(prefixes):
    sum = 0
    for prefix,val in prefixes.iteritems():
        sum += val[2]
    return sum

"""
Creates prefix cumulative probability distribution
"""
def create_cumul_fxn(prefix_order, prefixes, total_prob):
    cumul_prob = 0
    prefix_cumul = {}
    for prefix in prefix_order:
        prefix_cumul[prefix] = cumul_prob
        cumul_prob += float(prefixes[prefix][2]) / total_prob
    return prefix_cumul

"""
Creates list of ordered prefixes
"""
def create_prefix_ordered_list(prefixes):
    return sorted(prefixes,key = prefixes.get)

"""
Create inverse sampling table
"""
def create_inverse_sample_table():
    with open('inverse_table.txt','r') as f:
        table = eval(f.read())
    return table

# given random message string as int, return int message with last digit appended such that new string is Luhn-valid
def luhn(m):
    sum = 0
    for i in list(str(m)):
        sum += int(i)
    last = (9 * sum) % 10
    return m * 10 + last

class CreditCardProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, prefixes):
        self.prefixes = prefixes
        self.prefix_order = create_prefix_ordered_list(prefixes)
        self.total_prob = getTotalProbability(prefixes)
        self.prefix_cumul = create_cumul_fxn(self.prefix_order, prefixes, self.total_prob)
        self.inverse_table = create_inverse_sample_table()


        # define probability distribution fxn
        # this actually doesn't depend on the prefix but only the length of the string....
        # whatever
        def prob(self, m):
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                prefixStr = ''.join(prefix)
                if prefixStr in self.prefixes:
                    prefixProb = 1.0 / self.total_prob
                    #last digit is the check dig
                    randomDigs = m[6:-1]
                    numRandomDigs = len(randomDigs)
                    prob = prefixProb * math.pow(10,-numRandomDigs)
                    return prob
            print "Invalid credit card"
            return 0

        # define cumul distribution fxn
        def cumul(self, m):
            #print m
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                prefixStr = ''.join(prefix)
                if prefixStr in self.prefixes:
                    #last digit is the check dig
                    randomDigs = m[6-self.prefixes[prefixStr][0]:-1]
                    numRandomDigs = self.prefixes[prefixStr][1] - 7
                    prefixCumul = self.prefix_cumul[prefixStr]
                    totalCumul = prefixCumul + float(randomDigs)*pow(10,-numRandomDigs) / self.total_prob
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

    
