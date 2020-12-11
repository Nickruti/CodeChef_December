# cook your dish here
import random
import math
testcases = int(input())

for i in range(testcases):
    N, K = input().split()
    N = int(N)
    K = int(K)
    seq = []
    even = 0
    odd = 0
    if N%2==0:
        even = 1
    else:
        odd = 1
        
    #for loop to generate alternative positive and negative sequence
    for i in range(1, N+1):
        if ((i%2==0) and even) or ((i%2!=0) and odd):
            seq.append(i)
        else:
            seq.append(-i)
            
    #cntP holds number of positive umbers in sequence       
    cntP = math.ceil(N/2)
    
    #K is greater than CntP and N is odd
    if (K > cntP) and odd:
        for i in range(N-1, -1, -1):
            if (i+1)%2==0:
                seq[i] = i+1
                cntP += 1
                if cntP == K:
                    break
                    
    #K is reater than CntP and N is even            
    elif (K > cntP) and even:
        for i in range(N-1, -1, -1):
            if (i+1)%2!=0:
                seq[i] = i+1
                cntP += 1
                if cntP == K:
                    break
                    
    #K is less than CntP and N is odd            
    elif (K < cntP) and odd:
        for i in range(N-1, -1, -1):
            if (i+1)%2!=0:
                seq[i] = -(i+1)
                cntP -= 1
                if cntP == K:
                    break
                    
    #K is less than CntP and N is even            
    elif (K < cntP) and even:
        for i in range(N-1, -1, -1):
            if (i+1)%2==0:
                seq[i] = -(i+1)
                cntP -= 1
                if cntP == K:
                    break
    
    print(" ".join(map(str, seq)))
    
    
