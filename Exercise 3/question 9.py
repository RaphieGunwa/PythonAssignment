def count_elements_within_range(arr, min_value, max_value):
    count = sum(1 for num in arr if min_value <= num <= max_value)
    return count

# Example with a list, minimum value and maximum value
my_list = [24, 12, 2, 17, 3, 7, 3, 15]
minimum_value = 2
maximum_value = 24
result = count_elements_within_range(my_list, minimum_value, maximum_value)
print("The number of elements within the range is:", result)
