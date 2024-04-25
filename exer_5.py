Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = int(input("Enter the Number: "))
pair = []

for i in range(0, len(Numbers)):  
    for j in range(0, len(Numbers)):  
        if (Numbers[i]+ Numbers[j]) == n:
           
            if [Numbers[i],Numbers[j]]  not in pair and [Numbers[j],Numbers[i]]  not in pair:
                    pair.append([Numbers[i],Numbers[j]])
                  
            
print(pair)    
 