# cook your dish here
import math

testcases = int(input())
for i in range(testcases):
    N, D = input().split()
    people_ages = list(map(int, input().split()))
    
    atRisk = 0
    notAtRisk = 0
    for i in people_ages:
        if (i >= 80) or (i <= 9):
            atRisk += 1
        else:
            notAtRisk += 1
    
    print(math.ceil(atRisk/int(D)) + math.ceil(notAtRisk/int(D)))

