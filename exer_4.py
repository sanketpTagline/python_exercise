number= int(input("Enter the Number :"))

# fibonacci series in recursive menner

def fibo(n):
    if n <=1:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(number):
    print(fibo(i))

#  fibonacci series in memoization menner

cache = {0:0,1:1}

def fibonacci(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

fibonachi_memo = [fibonacci(n) for n in range(number)]
print("\n",fibonachi_memo)

# Create a recursion function that calculate the sum of numbers present in the list.
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
 
def list_sum(n):
    if not n:
        return 0
    else:
        return n[0] + list_sum(n[1:])   
    
total_sum = list_sum(numbers)
print("\n Sum of List is :",total_sum)