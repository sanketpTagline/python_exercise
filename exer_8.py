numbers = [2, 5, 6, 1, 3, 8, 9, 10]

for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        if (numbers[i]< numbers[j]):
            numbers[i],numbers[j] = numbers[j],numbers[i]
            
print(numbers)