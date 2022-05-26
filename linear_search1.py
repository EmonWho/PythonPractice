from pyparsing import line

def linear_search_prc(list,target):
  for i in range(0,len(list)):
    if list[i]==target:
      return i
      return None

def verify(index):
  if index is not None:
    print("target is in index :",index) 
  else:
    print("Taget is not in list .")

numbers= [10,14,19,26,27,31,33,35,42,44]
result=linear_search_prc(numbers,35)
verify(result)             
