# cook your dish here
import math
arr = list(map(int, input().split()))
days = 1
if arr[0] == arr[2] == 1:
    days = math.ceil(arr[4]/(arr[1] + arr[3]))
else:
    cntV = 0
    days = min(arr[0], arr[2])-1
    d1 = arr[0]
    d2 = arr[2]
    while cntV < arr[4]:
        if d1 < d2:
            cntV = cntV + arr[1]
            days += 1
            d1 += 1
            
        elif d2 < d1:
            cntV = cntV + arr[3]
            days += 1
            d2 += 1
            
        else:
            cntV = cntV + arr[1] + arr[3]
            days += 1
        
print(days)
