from itertools import combinations
numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
sum = int(input("Enter the Number: "))

comb = [[a,b] for [a,b] in combinations(numbers,2) if a+b == sum]
uniqueCombination = []
for [a,b] in comb:
    if [a,b] in uniqueCombination or [b,a] in uniqueCombination:
        continue
    else:
        uniqueCombination.append([a,b])
print(uniqueCombination)