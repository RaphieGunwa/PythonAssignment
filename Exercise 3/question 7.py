def last_index_of_value(arr, value):
    if value in arr:
        return len(arr) - arr[::-1].index(value) - 1
    else:
        return -1

# Example usage with a list and an integer value
my_list = [74, 85, 102, 99, 101, 85, 56]
value = 85
result = last_index_of_value(my_list, value)
print("The last index of the value", value, "is:", result)
