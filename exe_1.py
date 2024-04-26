numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

#  A. Length of the list
list_length = len(numbers)

print("Length of the list: ",list_length)

# B. Display first 3 numbers
print("First 3 numbers: ",numbers[:3])

#  C. Display sum of odd numbers
def even_numbers(num):
    if(num%2 != 0):
        return True
    else:
        return False

evenNums = filter(even_numbers, numbers)
print("Sum of odd numbers: ",sum(evenNums))

#  D. Number of duplicate numbers   
duplicate = set()

for num in numbers:
    n = numbers.count(num)
    if n > 1:
           duplicate.add(num) 
           
print("Number of duplicate number : ",len(duplicate))
 
# E.Display list without duplicate numbers
distinct_list = []

for i in numbers:
    if i not in distinct_list:
        distinct_list.append(i)
        
print("List without duplicate numbers: ",distinct_list)