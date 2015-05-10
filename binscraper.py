import urllib2
import re

# Script to scrape BIN #s off Wikipedia page for use in 
# probability distribution construction

# Get HTML source of webpage
def getSource(url):
    response = urllib2.urlopen(url)
    return response.read()

# Matches IINs in inputted text
# Output: dictionary of BIN numbers with format (BIN #, random digits)
def matchStrings(text):
    bins = {}
    m = re.compile("[^0-9][0-9\*]{6}[^0-9]")
    for i in range(len(text)):
        if m.match(text[i:i+8]):
            iin = text[i+1:i+7]
            j = 0
            while j < len(iin) and iin[j] != '*':
                j += 1
            if iin in bins:
                pass
            else: 
                bins[iin] = [6 - j]
    return bins

def stringify(range):
    list = []
    for i in range:
        list.append(str(i))
    return list

def addLengths(data):
    # for p in data:
    #     if p[0:1] == '34' or p[0:1] == '37':
    #         data[p].append(15)
    #     elif p[0:3] == '5610' or p[0:5] in stringify(range(560221, 560226)):
    #         data[p].append(16)
    #     elif p[0:1] == '62':
    #         data[p].append('16-19')
    #     elif p[0:3] in ['2014', '2149']:
    #         data[p].append(14)
    #     elif p[0:2] in stringify(range(300,306)) or p[0:2] == '309':
    #         data[p].append(14)
    #     elif p[0:1] in ['36', '38', '39']:
    #         data[p].append(14)
    #     elif p[0:1] == ['54', '55']:
    #         data[p].append(16)
    #     elif p[0:4] == '6011' or p[0:3] in stringify(range(644, 650)):
    #         data[p].append(16)
    #     elif p[0:2] == '636':
    #         data[p].append(16)
    #     elif p[0:5] in stringify(range(500000, 510000)) or p[0:5] in stringify(range(560000, 700000)):
    #         data[p].append('12-19')
    #     elif p[0:5] in stringify(range(622126,622926)):
    #         data[p].append(16)
    #     elif p[0:2] in stringify(range(644, 649)):
    #         data[p].append(16)
    #     elif p[0:1] == '65':
    #         data[p].append(16)
    #     elif p[0:2] in stringify(range(637, 639)):
    #         data[p].append(16)
    #     elif p[0:3] in stringify(range(3528, 3590)):
    #         data[p].append(16)
    #     elif p[0:3] == '6304' or p[0:3] == '6706' or p[0:3] == '6771' or p[0:3] == '6709':
    #         data[p].append('16-19')
    #     elif p[0:3] in stringify([5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763]):
    #         data[p].append('16-19')
    #     elif p[0:1] in stringify(range(51,56)):
    #         data[p].append('16-19')
    #     elif p[0] == '4':
    #         data[p].append(16)
    #     elif p[0:3] in stringify([4026, 4508, 4844, 4913, 4917]):
    #         data[p].append(16)
    #     elif p[0:5] == '417500':
    #         data[p].append(16)
    #     else:
    #         data[p].append(False)
    return data

def analyze(data):
    true = 0
    false = 0
    for i in data:
        if data[i][1]:
            true += 1
        else:
            false += 1
    return 'True: ' + str(true) + '\n' + 'False: ' + str(false)

# Writes data in contents to file specified by filepath.
# Input: f
ilepath path to file to be written to
#        contents dictionary of keys to be written
def writeFile(filepath, contents):
    # Clear file if not empty
    open(filepath, 'w').close()
    # Write to file
    f = open(filepath, 'w')
    f.write(str(contents))
    # for j in contents:
    #     f.write(j + ', ' + str(contents[j]) + '\n')

if __name__ == '__main__':
    src = getSource("http://www.stevemorse.org/ssn/List_of_Bank_Identification_Numbers.html")
    writeFile('bin.txt', addLengths(matchStrings(src)))
    # print analyze(addLengths(matchStrings(src)))





