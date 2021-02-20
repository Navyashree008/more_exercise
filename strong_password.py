user = input("enter your password")
if len(user) >= 6 or len(user) <= 16:
    if '$' in user:
        if 2 or 8 in user:
            if 'A' or 'Z' in user:
                print("its a strong password")
            else:
                print("not a strong pasword")    
        else:
            print("not a strong pasword")
    else:
        print("not a strong pasword")
else:
    print("not a strong password")