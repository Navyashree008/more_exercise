i = 1
while i <= 1000:
    a = list(str(i)) 
    j = 0
    sum = 0
    while j < len(a):
        digit = int(a[j])
        sum = sum + digit
        j+=1
    if i % sum == 0:
        print(i,"its harshad number")
    else:
        print(i,"its not")
    i+=1
    