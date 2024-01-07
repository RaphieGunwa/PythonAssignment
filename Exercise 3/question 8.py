def calculate_range(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_value = max_value - min_value + 1
    return range_value

# Example usage with a list
my_list = [16, 22, 27, 49, 36, 13, 72]
result = calculate_range(my_list)
print("The range of the list is:", result)
