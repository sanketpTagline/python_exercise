GP = [3, 6, 9, 12, 16, 18]
AP =[2, 5, 8, 11, 15, 17]

def checkAP(ap_list):
    a = ap_list[0]
    d = ap_list[1]-ap_list[0]
    
    for n in range(1,len(ap_list)-1): 
        if (ap_list[n + 1] - ap_list[n]) != (ap_list[n-1] - ap_list[n-2]):
            print(ap_list[n-1])
            ap_list[n+1] = a + ((n+1) * d)
            
    print(ap_list)

def checkGP(gp_list):
    a = gp_list[0]
    r = gp_list[1] / gp_list[0]
    
    for i in range(2,len(gp_list)):
        if (gp_list[i] / gp_list[i - 1] != r):
            gp_list[i] = int(a * r**(i))
                   
    print(gp_list)

print(checkAP([2, 5, 8, 11, 15, 17]))    
print(checkGP([1,2,4,8,16,30,64,128,254,510]))