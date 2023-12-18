input_str = input("Enter a string: ")

if len(input_str) < 2:
    result_str = ""
else:
    result_str = input_str[:2] + input_str[-2:]

print("Result:", result_str)