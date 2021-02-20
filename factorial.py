# num = int(input("enter the number"))
# if num > 0:
#     i = 1
#     fac = 1
#     while i <= num:
#         fac = fac*i
#         i+=1
#     print(fac)
# else:
#     print("input should be any positive number")

# function:-
def factorial(num):
    if num > 0:
        i = 1
        fac = 1
        while i <= num:
            fac = fac*i
            i+=1
        return fac
    else:
        return 'enter positive number'
num = int(input("enter the number"))
print(factorial(num))
