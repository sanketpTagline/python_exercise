GP = [3, 6, 9, 12, 16, 18]
AP =[2, 5, 8, 11, 15, 17]

def checkAP(list):
    a = list[0]
    d = list[1]-list[0]
    
    for n in range(1,len(list)-1): 
        if (list[n + 1] - list[n]) != (list[n-1] - list[n-2]):
            print(list[n-1])
            list[n+1] = a + ((n+1) * d)
            
    print(list)

def checkGP(list):
    a = list[0]
    r = list[1] / list[0]
    
    for i in range(2,len(list)):
        if (list[i] / list[i - 1] != r):
            list[i] = int(a * r**(i))
                   
    print(list)

print(checkAP([2, 5, 8, 11, 15, 17]))    
print(checkGP([1,2,4,8,16,30,64,128,254,510]))