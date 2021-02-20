# # through looping:-
i = 1
while i <= 1000:
    if i % 21 == 0:
        print("navgurukul")
    elif i % 7 == 0:
        print("gurukul")
    elif i % 3 == 0:
        print("nav")
    else:
        print(i)
    i+=1

#  fuction:-
def navgurukul(i):
    for i in range(i,1001):
        if i % 21 == 0:
            print("navgurukul")
        elif i % 7 == 0:
            print("gurukul")
        elif i % 3 == 0:
            print("nav")
        else:
            print(i)
navgurukul(1)


