def sum_of_elements(numbers, exclude_negative = False):
    if exclude_negative:
        return sum(num for num in numbers if num >= 0)
    else: return sum(numbers)

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")   
    input_list = user_input.split() 
    numbers = list(map(int, input_list))
    exclude_choice = input("Do you want to exclude negative numbers? (yes/no): ").lower()
    exclude_negative = True if exclude_choice == 'yes' else False

    result = sum_of_elements(numbers, exclude_negative)
    print(f"Sum of elements: {result}")

if __name__ == "__main__":
    main()