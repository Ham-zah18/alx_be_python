pattern = int(input("Enter the size of the pattern: "))

count = 0

while pattern > count:
    for i in range(pattern):
        print("*", end="")
    print()  # Move to a new line after each row of asterisks
    count += 1