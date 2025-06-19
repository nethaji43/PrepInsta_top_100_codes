number1=int(input("enter a number1: "))
number2=int(input("enter a number2: "))
number3=int(input("enter a number3: "))

if (number1 > number2) and (number1>number3):
    print(f"{number1} is greatest number than {number2} and {number3}")
elif (number2 >number3) and (number2>number1):
    print(f"{number2} is greatest number than {number1} and {number3}")
elif (number3>number1) and (number3>number2):
    print(f"{number3} is greatest number than {number2} and {number1}")
else:
    print(f"{number1} , {number2} and {number3} are equal.")