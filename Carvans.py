'''
Problem url - https://www.codechef.com/LRNDSA01/problems/CARVANS
'''

for i in range(int(input())):
    N = int(input())
    carSpeeds = list(map(int, input().split()))
    
    for j in range(len(carSpeeds)-1):
        if carSpeeds[j] < carSpeeds[j+1]:
            carSpeeds[j+1] = carSpeeds[j]
            N = N - 1
    print(N)
