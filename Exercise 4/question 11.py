def printRange(num1, num2):
    if num1 < num2:
        for i in range(num1, num2 + 1):
            print(i, end="")
    elif num1 > num2:
        for i in range(num1, num2 - 1, -1):
            print(i, end=" ")
    else:
        print(num1)

# Test the printRange method
printRange(2, 7)  
print("\n")
printRange(19, 11)
print("\n")
printRange(5, 5)  
