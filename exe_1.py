numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

#  A. Length of the list
list_length = len(numbers)
print("Length of the list:",list_length)

# B. Display first 3 numbers
print("First 3 numbers:",numbers[:3])

#  C. Display sum of odd numbers
sum_odd_number = [num for num in numbers if num%2!=0]
print("Sum of odd numbers: ",sum(sum_odd_number))

#  D. Number of duplicate numbers
    
duplicate_list =[]     

 
for i in range(0, len(numbers)):    
    for j in range(i+1, len(numbers)):    
        if(numbers[i] == numbers[j]):    
            if numbers[i] not in duplicate_list:
                duplicate_list.append(numbers[i])

print("Number of duplicate numbers: ",len(duplicate_list))


# E.Display list without duplicate numbers

distinct_list = []

for i in numbers:
    if i not in distinct_list:
        distinct_list.append(i)
        
print("List without duplicate numbers: ",distinct_list)