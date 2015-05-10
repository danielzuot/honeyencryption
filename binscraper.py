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

# Helper method to turn int list into list of strings
def stringify(array):
    list = []
    for i in array:
        list.append(str(i))
    return list

# Gives each prefix a probability numerator
def getPrefixProbability(bin):
    [bin[i].append(10**(bin[i][0])) for i in bin]
    return bin

# Gives each prefix a total card length
def addLengths(data, prefix_length_dict):
    for i in prefix_length_dict:
        prefixes = prefix_length_dict[i][1:]
        length = prefix_length_dict[i][0]
        for prefix in prefixes:
            for s in prefix:
                for p in data:
                    if p[0:len(str(s))-1] == str(s):
                        data[p].append(length)
    for p in data:
        if len(data[p]) < 2:
            data[p].append(False)
    return data

def analyze(data):
    true = 0
    false = 0
    for i in data:
        if data[i][1] != False:
            true += 1
        else:
            false += 1
    return 'True: ' + str(true) + '\n' + 'False: ' + str(false)

def getData():
    f = open('bin.txt', 'r')
    return eval(f.read())

# Writes data in contents to file specified by filepath.
# Input: filepath path to file to be written to
#        contents dictionary of keys to be written
def writeFile(filepath, contents):
    # Clear file if not empty
    open(filepath, 'w').close()
    # Write to file
    f = open(filepath, 'w')
    f.write(str(contents))

if __name__ == '__main__':
    src = getSource("http://www.stevemorse.org/ssn/List_of_Bank_Identification_Numbers.html")
    f = open('prefix_lengths.txt', 'r')
    writeFile('bin.txt', getPrefixProbability(addLengths(matchStrings(src), eval(f.read()))))





