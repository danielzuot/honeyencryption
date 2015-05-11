# generate_inverse_table.py

# Generates inverse sampling table for the credit card space


from credit_card import *

with open('bin.txt','r') as bin:
    prefixes = eval(bin.read())

'''
prefixes = {
    '5235**': [2, 8, 100],
    '123456': [0, 8, 1]
}
'''
total_prob = getTotalProbability(prefixes)
prefix_order = create_prefix_ordered_list(prefixes)
prefix_cumul = create_cumul_fxn(prefix_order, prefixes, total_prob)
table = open('inverse_table.txt','w')
for prefix in prefix_order:
    #'******'
    prefixList = list(prefix)
    prefix_cumul_prob = prefix_cumul[prefix]
    prefix_length = prefixes[prefix][1]
    degs_freedom = prefix.count('*')
    for i in range(10**degs_freedom):
        paddedStr = str(i).zfill(degs_freedom)
        for k in range(degs_freedom):
            prefixList[6-degs_freedom+k] = paddedStr[k] 
        newPrefix = ''.join(prefixList)
        m = str(luhn(int(newPrefix+'0'*(prefix_length-7))))
        randomDigs = m[6-degs_freedom:-1]
        numRandomDigs = prefix_length - 7
        cumul_prob = prefix_cumul_prob + float(randomDigs)*pow(10,-numRandomDigs) / total_prob
        table.write('('+str(cumul_prob)+',"'+str(m)+'"),\n')
