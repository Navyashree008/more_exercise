def numbers_less_than_twenty(list):
  i = 0
  while i < len(list):
    item = list[i]
    if item > 20:
      list.remove(item)
    else:
      i += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
store_list = num_list.copy()
num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", store_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20) 