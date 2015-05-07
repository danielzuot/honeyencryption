# generic_alphabet.py

# Creation of the proper probability functions required
# (cumul_distr, prob_distr, next_message, get_inverse_cumul_distr_samples)
# to create a MessageSpaceProbabilityFxns object that represents
# the message space of an arbitrary generic alphabet given only a
# alphabet, letter probabilities, message length.

"""
Requires generic alphabet specifications:
alphabet : list of letters in alphabet (determines ordering for cumul)
letter_prob : dict of letter to probability - sum of all letters is 1
msg_len : number of letters per message
"""

import probabilityfunctionAPI


"""
Creates letter cumulative probability distribution
"""
def create_cumul_fxn(alphabet, letter_prob):
    cumul_prob = 0
    letter_cumul = {}
    for l in alphabet:
        letter_cumul[l] = cumul_prob
        cumul_prob += letter_prob[l]
    return letter_cumul

"""
Creates letter to order dictionaries
"""
def create_letter_order_dict(alphabet):
    letter_to_order = {}
    for i in range(len(alphabet)):
        letter_to_order[alphabet[i]] = i
    return letter_to_order

"""
Create inverse sampling table
"""
def create_inverse_sample_table(alphabet, letter_cumul, msg_len):
    table = [] #(prob, m)
    pad = alphabet[0]*(msg_len - 1)
    for l in alphabet:
        table.append((letter_cumul[l], l + pad))
    return table


class GenericAlphabetProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, alphabet, letter_prob, msg_len):
        self.alphabet = alphabet
        self.letter_prob = letter_prob
        self.msg_len = msg_len
        self.letter_cumul = create_cumul_fxn(alphabet, letter_prob)
        self.letter_order = create_letter_order_dict
        self.inverse_table = create_inverse_sample_table(alphabet, self.letter_cumul, msg_len)

        # define probability distribution fxn
        def prob(m):
            # product of each letter's probability
            product = 1
            for l in m:
                product *= self.letter_prob[l]
            return product

        # define cumul distribution fxn
        def cumul(m):
            # product of each letter's cumulative probability
            product = 1
            for l in m:
                product *= self.letter_cumul[l]
            return product

        # define next message fxn
        def next_msg(m):
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
        def get_inverse_table():
            return self.inverse_table

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxns.__init__(self, cumul, prob, next_msg, get_inverse_table)

    
