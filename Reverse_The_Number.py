'''
Problem url - https://www.codechef.com/LRNDSA01/problems/FLOW007
'''

testcases = int(input())
for i in range(testcases):
    num = int(input())
    rev = 0
    while num > 0:
        remain = (num % 10)
        rev = (rev * 10) + remain
        num = num // 10
    print(rev)
