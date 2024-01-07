def smallestLargest():
    num = int(input("How many numbers do you want to enter? "))
    
    if num > 0:
        numbers = [int(input(f"Number {i + 1}: ")) for i in range(num)]
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Smallest = {smallest}")
        print(f"Largest = {largest}")
    else:
        print("Please enter a valid number greater than 0 for the number of numbers to read.")

# Test the smallestLargest method
smallestLargest()
