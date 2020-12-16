'''
Prolem url - https://www.codechef.com/LRNDSA01/problems/ZCO14003
'''

# cook your dish here
arr = []
for i in range(int(input())):
    arr.append(int(input()))
max_revenue = 0
arr.sort()
len_ = len(arr)
for i in range(len_):
    revenue = arr[i] * (len_-i)
    if max_revenue < revenue:
        max_revenue = revenue

print(max_revenue)
    
