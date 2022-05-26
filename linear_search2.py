def ls(list,target):
  for li in range(1,len(list)):
   if list[li]==target: 
    return li
    return -1

def verify(index):
  if index is not -1:
    print("The target is in List where index no is ", index)
  else:
    print("The target is not in list .")

number_list=[10,12,14,15,11,17]      
result=ls(number_list,11)

verify(result)