number1=int(input("enter a number1:"))
number2=int(input("enter a number2:"))
if number1>number2:
    print(f"{number1} is greatest number than {number2}")
elif number2>number1:
    print(f"{number2} is greatest number than {number1}")
else:
    print(f"{number1} and {number2} numbers  are same.")
