def swap_elements(arr, index1, index2):
    if 0 <= index1 < len(arr) and 0 <= index2 < len(arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]

# Example usage with a list and two indexes
my_list = [3, 7, 12, 5, 9]
swap_elements(my_list, 1, 3)
print(my_list)  # Output: [3, 5, 12, 7, 9] - Elements at indexes 1 and 3 have been swapped
