number = int(input("Enter a number: "))

factorialno = 1

for i in range(1, number + 1):
    factorialno *= i

print("The factorial of number is: ", factorialno)