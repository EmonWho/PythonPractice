#/ First step using Extended sclicing 
"""
"""
"""input='Hello'
print(input[-1::-1])

""""""
"""



#/ Second step using for loop
""" inputStr='Wellcome'
result=''

for i in range(len(inputStr)-1,-1,-1):
    result=result + inputStr[i]

print(result)  """


#/ Third step using Reversed String 
inputString='Welcome'

reverseChar=reversed(inputString)
print(''.join(reverseChar))
