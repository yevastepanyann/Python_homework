def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0: 
            even_numbers.append(num)
        else: odd_numbers.append(num)
    return odd_numbers, even_numbers    

user_input = input("Enter numbers separated by space: ")
input = user_input.split()
numbers = list(map(int, input))
odd_numbers, even_numbers = classify_numbers(numbers)
print(f"Even numbers:{even_numbers}")
print(f"Odd numbers:{odd_numbers}")



