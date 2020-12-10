# cook your dish here
import math
testcase = int(input())

for i in range(testcase):
    A, B = input().split()

    cntAE = math.floor(int(A)/2)
    cntAO = int(A) - cntAE
    cntBE = math.floor(int(B)/2)
    cntBO = int(B) - cntBE
     
    evens = 0   
    evens += cntAE * cntBE
    evens += cntAO * cntBO
    
    print(evens)
        
        
