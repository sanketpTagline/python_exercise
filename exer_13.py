import functools

class Number:
    def __init__(self, numbers):
        self.numbers = numbers
         
    def get(self):
        return self.numbers

    def change_original_values(self, func: lambda x: x): 
        new_numbers = list(map(func, self.get()))
        return new_numbers

    def filter_values(self, filter_func: lambda x: x):
        filtered_numbers =  list(filter(filter_func,self.get()))
        return filtered_numbers

    def compound_the_numbers(self, reduce_func: lambda a, b: a + b): 
        compounded_value = functools.reduce(reduce_func,self.get())
        return compounded_value

    def sort(self):
        return sorted(self.numbers)

if __name__ == "__main__": 
    numbers = [2, 5, 1, 66, 22, 11, 10]

    n1 = Number(numbers)
     
    print("Numbers: ", n1.get())
    
    lambda_func1 = lambda number : number * 2
    print("New values:", n1.change_original_values(func=lambda_func1))

    lambda_func2 = lambda number: number % 2 == 0
    print("Filtered values:", n1.filter_values(filter_func=lambda_func2))
    
    lambda_func3 = lambda compound,number: compound + number
    print("Compounded value:", n1.compound_the_numbers(reduce_func=lambda_func3))

    print("Sorted list:", n1.sort())
 
 
  
 