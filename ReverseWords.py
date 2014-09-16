#Reverse words of sentences challenge on CodeEval, not reverse characters.

import sys
import re

test_cases = open(sys.argv[1], 'r')
array = []

for test in test_cases:
    if test.strip():     #this take cares of the empty line during read-in

        #print test.strip()        #.strip() to remove the blank line after each print

        array = re.split(' |,|\\n|"|\(|\)|\'',test.strip())    #split the input into an array
        max = len(array)
        i = 1
        line = ""

        for cell in array:
            line = line +array[max-i]+" "
            i+=1
        print line.strip()

test_cases.close()
