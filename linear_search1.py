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

numbers= [1,2,3,4,5,6,7,8,9]
result=linear_search_prc(numbers,8)
verify(result)             
