pos = -1
def binarysort(list,n):
  l = 0
  u = len(list)-1

  
  while l<=u :
    mid= (l+u)//2  

    if list[mid] == n:
       globals()['pos'] = mid
       return True
    else:
       if list[mid] < n:
         l = mid;
       else:
        u = mid;   

list = [10,12,14,15,16,18,22,24,26,70]
n = 24

if binarysort(list,n):
  print("Found at", pos+1)
else:
  print("Not Found")  