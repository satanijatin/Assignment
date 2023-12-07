
n = int(input("Enter a positive integer : "))


if n <= 0:
    print("Please enter a positive integer.")
else:

    sumofintegers = sum(range(1, n + 1))
  
    print("The sum of the positive integers is: ", sumofintegers)
