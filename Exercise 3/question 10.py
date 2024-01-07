def is_been_sorted(input_list):
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

print(is_been_sorted(list1))  # This will print False
print(is_been_sorted(list2))  # This will print True
