
inputstring = (str(input("Enter String: ")))


if len(inputstring) % 4 == 0:
 
    reversedstring = inputstring[::-1]
    print("Reversed String: ",reversedstring)
else:
    print("Original String:",inputstring)