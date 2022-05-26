def binary_search(list,target):
  first=0
  last = len(list)-1

  while first <= last:
   midpoint = (first+last)//2

   if list[midpoint]==target:
     return midpoint
   elif list[midpoint]<target:
     first= midpoint+1
   else:
      first= midpoint-1

  return None    

def verify(index):
  if index is not None:
    print("The target is in list and Index no is .",index)
  else:
    print("The target not in list .")  

number=[10,20,30,40,50,60,70]    
result=binary_search(number,40)

verify(result)