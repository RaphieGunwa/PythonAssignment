# Initialize sum and number variables
total_sum = 0
number = 0

# Prompt user for numbers until -1 is entered
while number != -1:
    number = int(input("Enter a number (-1 to stop): "))
    if number != -1:
        total_sum += number  # Add the entered number to sum

# Output the total sum
print("The sum of the numbers is:", total_sum)
