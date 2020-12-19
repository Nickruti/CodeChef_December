'''
Problem url - https://www.codechef.com/LRNDSA01/problems/FCTRL
'''

for i in range(int(input())):
    divisor = 5
    count = 0
    num = int(input())
    while (num/divisor) >= 1:
        count += (num//divisor)
        divisor *= 5
    print(count)
        
