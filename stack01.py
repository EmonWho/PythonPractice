def create():
    stack = []
    return stack
        
def stack_empty(stack):
    return(len(stack)==0)
   
def push(stack,item):
    stack.append(item)
    return("Pushed item " + item)
    
def pop(stack):
    if (stack_empty(stack)):
        return "Stack is empty "
    
    return stack.pop()

stack=create()
push(stack, str(2))
push(stack, str(4))
push(stack, str(10))
print("Popped item " + pop(stack))
print("After popping :" + str(stack))
