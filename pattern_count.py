#!/bin/python

import sys


def patternCount(s):
    l = len(s)
    count = 0
    
    i = 0
    
    while(i<l):
        if s[i] == '1':
            pattern_found = False
            # do check for pattern
            j = i+1 
            while(j<l and s[j]=='0'):
                pattern_found = True
                j +=1
            #now we have looped over the 0's
            #case: 10001
            if j<l and s[j]=='1' and pattern_found == True:
                count += 1
            i = j
        else:
            i+=1
            
    return count
        
        


                    
        

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)


