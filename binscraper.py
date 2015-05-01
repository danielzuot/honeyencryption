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
                bins[iin] = 6 - j
    return bins

# Writes data in contents to file specified by filepath.
# Input: filepath path to file to be written to
#        contents dictionary of keys to be written
def writeFile(filepath, contents):
    # Clear file if not empty
    open(filepath, 'w').close()
    # Write to file
    f = open(filepath, 'w')
    for j in contents:
        f.write(j + ', ' + str(contents[j]) + '\n')

if __name__ == '__main__':
    src = getSource("http://www.stevemorse.org/ssn/List_of_Bank_Identification_Numbers.html")
    writeFile('bin.txt', matchStrings(src))