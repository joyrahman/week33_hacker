# week33_hacker
#!/bin/python

import sys

def twinArrays(ar1, ar2):
    # Complete this function
    
    #approach, find index,val of min of both arrays
    x = find_min(ar1,-1)
    y = find_min(ar2,-1)
    #if indexes are not same, return result.
    if x != y :
        return ar1[x]+ ar2[y]
    
    else:
        if ar1[x] < ar2[y]:
            #search in ar2
            z = find_min(ar2,y)
            return ar1[x] + ar2[z]
        else:
            #search in ar1
            z = find_min(ar1,x)
            return ar2[y] + ar1[z]
    #else
    # pick the min among the two. search for the other one on other array
    
    
def find_min(ar, pos):
    local_min = sys.maxint
    l = len(ar)
    for i in xrange(0,l):
        
        if pos!= i and ar[i] <local_min:
            local_min  = ar[i]
            local_min_index = i
    
    return local_min_index

n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)




