'''
-----------APRIL CHALLANGES------------

Problem 2 - https://www.codechef.com/APRIL21C/problems/BOLT

Statement - Given Chef's max speed v during practice and the factors k1,k2,k3, find whether he will be able to create a new world record,
i.e, can he complete 100 m in less than 9.58 seconds?

'''
for _ in range(int(input())):
    k1, k2, k3, v = input().split()
    
    finalSpeed = float(k1)*float(k2)*float(k3)*float(v)
    newTime = float(100/finalSpeed)
    if round(newTime, 2) < 9.58:
        print("YES")
    else:
        print("NO")
