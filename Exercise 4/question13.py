def printAverage():
    total = 0
    count = 0

    while True:
        number = int(input("Type a number: "))
        if number < 0:
            if count == 0:
                print("No nonnegative numbers were entered.")
            else:
                average = total / count
                print(f"Average was {average:.1f}")
            break
        total += number
        count += 1

# Test the printAverage method
printAverage()
