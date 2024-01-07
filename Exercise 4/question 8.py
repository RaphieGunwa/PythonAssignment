# Initialize sum and number variables
total_sum = 0
number = None

# Prompt user for numbers until 0 is entered
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break  # Break out of the loop if 0 is entered
    total_sum += number  # Add the entered number to the sum

# Output the total sum
print("The sum of the numbers is:", total_sum)
