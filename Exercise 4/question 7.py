low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
total_sum = 0

for i in range(low, high + 1):
    total_sum += i  # Accumulate the sum

print("sum =", total_sum)
