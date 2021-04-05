'''
----------- April Challenges ---------------

Problem 3- https://www.codechef.com/APRIL21C/problems/SSCRIPT

Statement - A string is said to be using strong language if it contains at least K consecutive characters '*'.
You are given a string S with length N. Determine whether it uses strong language or not.

'''
def sscript(word, n, k):
    count = 0
    flag = 0
    for i in range(int(n)):
        if word[i] == '*':
            count += 1
        else:
            if count == int(k):
                return 1
            count = 0   
    if count == int(k):
        return 1
    else:
        return 0
            
for _ in range(int(input())):
    n, k = input().split()
    word = input()    
    value = sscript(word, n, k)   
            
    if value == 0:
        print("NO")
    else:
        print("YES")
