def binary_search1(list,target):
  first = 0
  last = len(list)-1

  while first <= last:
   midpoint =(first + last)//2   

   if list[midpoint] == target:
     return midpoint
   elif list[midpoint]<target:
     first=midpoint + 1
   else:
     first = midpoint - 1
   
  return None    

def verify(index):
  if index is not None:
    print("The target is in list and index no is :",index)
  else :
    print("The target is not in list")  
   
number = [11,13,15,17,19,21,23,25]
print("The numbers are ",number)
A=23

print("The searching number is ",A)
result = binary_search1(number,23)

verify(result)
    

