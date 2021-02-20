number_of_students = int(input("enter number"))
amount_per_student = int(input("enter amount"))
if number_of_students * amount_per_student <= 50000:
    print("budget ke andar hai")
else:
    print("budget ke bahar hai")

