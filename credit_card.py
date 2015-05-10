# credit_card.py

# Creation of the proper probability functions required
# (cumul_distr, prob_distr, next_message, get_inverse_cumul_distr_samples)
# to create a MessageSpaceProbabilityFxns object that represents
# the message space of credit cards.

"""
Requires: 

Dictionary of prefix-probabilities {'prefix',prob(prefix)}
Dictionary of prefix-lengths {'prefix',numberLength}

"""

from probabilityfunctionAPI import MessageSpaceProbabilityFxns


"""
Creates prefix cumulative probability distribution
"""
def create_cumul_fxn(prefix_prob):

    return []

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


class GenericAlphabetProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, prefix_prob, prefix_lengths):
        self.prefix_prob = prefix_prob
        self.prefix_lengths = prefix_lengths
        self.letter_cumul = create_cumul_fxn(prefix_prob)
        self.letter_order = create_prefix_ordered_list(prefix_prob)
        self.inverse_table = create_inverse_sample_table(alphabet, self.letter_cumul, msg_len)

        # define probability distribution fxn
        def prob(self, m):
            prefix = list('******')
            for i in range(6):
                prefix[i] = m[i]
                if ''.join(prefix) in self.prefix_prob:
                    
            

        # define cumul distribution fxn
        def cumul(self, m):
            # sum of each index cumulative contribution
            value = 0
            for i in range(1, self.msg_len)[::-1]:
                value += self.letter_cumul[m[i]]
                value *= self.letter_prob[m[i-1]]
            return value

        # define next message fxn
        def next_msg(self,m):
            least_sig_index = -1
            # Find index of message to increment letter
            for i in range(msg_len)[::-1]:
                if m[i] != alphabet[-1]:
                    least_sig_index = i
                    break
            if least_sig_index == -1:
                print "no next message - max message"
                return m
            # Increase letter order of index
            new_letter = self.alphabet[self.letter_order[m[least_sig_index]] + 1]
            return m[:least_sig_index] + new_letter + alphabet[0]*(self.msg_len - least_sig_index - 1)

        # create get sample table
        def get_inverse_table(self):
            return self.inverse_table

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxns.__init__(self, cumul, prob, next_msg, get_inverse_table)

    
