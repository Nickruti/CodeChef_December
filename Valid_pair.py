'''
April Challenges---

Problem 1 - https://www.codechef.com/APRIL21C/problems/SOCKS1

Statement - Chef has three socks in his drawer. Each sock has one of 10 possible colours, which are represented by integers between 1 and 10. 
Specifically, the colours of the socks are A, B, and C.
Chef has to wear two socks which have the same colour. Help Chef find out if that is possible or not.
'''
A,B,C = input().split()
if int(A)==int(B) or int(B)==int(C) or int(A)==int(C):
    print("YES")
else:
    print("NO")
