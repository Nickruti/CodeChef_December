# cook your dish here
import math
arr = list(map(int, input().split()))
if arr[0] == arr[2] == 1:
    days = math.ceil(arr[4]/(arr[1] + arr[3]))
else:
    if arr[0] > arr[2]:
        day2 = arr[0] - arr[2]
        sum1 = day2 * arr[3]
        day1 = arr[2] - 1

    else:
        day2 = arr[2] - arr[0]
        sum1 = day2 * arr[1]
        day1 = arr[0] - 1
    days = day1 + day2 + math.ceil((arr[4]-sum1)/(arr[1] + arr[3]))
print(days)
    

