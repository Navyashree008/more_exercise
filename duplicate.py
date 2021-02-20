# string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
# i = 0
# string_list2 = []
# while i < len(string_list):
#     if string_list[i] not in string_list2:
#         string_list2.append(string_list[i])
#     i+=1
# print(string_list2)

# function:-
def new_list(string_list):
    string_list2 = []
    for i in string_list:
        if i not in string_list2:
            string_list2.append(i)
    return string_list2
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
print(new_list(string_list))

