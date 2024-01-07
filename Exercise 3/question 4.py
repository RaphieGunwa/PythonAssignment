def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False  # Return False if the lists are not the same length
    
    return all(list1[i] < list2[i] for i in range(len(list1)))

# Example usage with two lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = compare_lists(list1, list2)
print(result)  # Output: True
