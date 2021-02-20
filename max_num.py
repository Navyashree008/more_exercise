num1 = int(input("enter number"))
num2 = int(input("enter number"))
num3 = int(input("enter number"))
if num1 > num2:
    if num1 >num3:
        print(num1,'is maximum')
elif num2 > num3:
    print(num2,'is maximum')
else:
    print(num3,'is maximum')
