mode = input("Enter math operation(+,-,*,/) or f for celcius to fahraheit conversion : ")
num1 = int(input("Enter first number :")) 
if mode == 'f':
    print(f"{num1} celsius is equivalent to {num1*9/5 + 32} fahraheit")
else:    
    num2 = int(input("Enter second number :"))

    if mode == "+":
        print(f"Answer is : {num1 + num2}")
    elif mode == "-":
        print(f"Answer is : {num1 - num2}")    
    elif mode == "*":
        print(f"Answer is : {num1 * num2}")   
    elif mode == "/":
        print(f"Answer is : {num1 / num2}")   
    else:
        print("input error")    