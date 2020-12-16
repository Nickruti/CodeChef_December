'''
Problem Url - https://www.codechef.com/LRNDSA01/problems/LAPIN
'''
# cook your dish here

try:
    for i in range(int(input())):
        sstr = input()
        l = len(sstr)//2
        
        if (len(sstr) % 2)==0:
            firsthalf = sstr[:l]
            secondhalf = sstr[l:]
        else: 
            firsthalf = sstr[:l]
            secondhalf = sstr[l+1:]
            
        if sorted(firsthalf) == sorted(secondhalf):
            print("YES")
        else:
            print("NO")
    
except:
    pass


    
