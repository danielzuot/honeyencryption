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
                    if p[0:len(str(s))] == str(s) and len(data[p]) < 2:
                        data[p].append(length)
    [data[p].append(16) for p in data if len(data[p]) < 2]
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

def remove(bin):
    bad = ['1*****', '0*****', '2*****', '3*****', '31****', '35****', '36****', '37****', '38****', '4*****', '40****', '41****', '42****', '43****', '44****', '45****', '46****', '47****', '48****', '49****', '5*****', '50****', '51****', '52****', '53****', '54****', '55****', '56****', '57****', '58****', '6*****', '60****','61****', '62****', '6200**', '6250**', '6270**', '6281**', '63****', '65****', '66****', '67****', '69****', '7*****', '89****', '8901**', '8914**', '8920**', '8934**', '8943**', '8944**', '8952**', '9*****', '9233**', '9752**', '9826**']
    for i in bad:
        if i in bin:
            del bin[i]
    return bin

def removeRepetitions(bin):
    newbin = {}
    newbin2 = {}
    for i in bin:
        if '*' in i:
            newI = re.sub('\*', '', i)
            for j in bin:
                if j != i:
                    if j.startswith(newI):
                        newbin[j] = bin[j]
    for m in bin:
        if m not in newbin:
            newbin2[m] = bin[m]
    print newbin2
    # writeFile('bin.txt', newbin2)

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
    g = open('bin.txt', 'r')
    # writeFile('bin.txt', getPrefixProbability(addLengths(matchStrings(src), eval(f.read()))))
    # print analyze(eval(g.read()))
    # print eval(g.read())
    # removeRepetitions(eval(g.read()))
    # writeFile('bin.txt', remove(eval(g.read())))





