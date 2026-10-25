class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "Cannot pop,stack is empthy"
        return self.items.pop()
    def top(self):
         if len(self.items)==0:
                    return "Cannot Top,stack is empthy"
         return self.items[-1]
    def size(self):
         return len(self.items)
    
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("stack content: ",stack.items)
print("popped item: ",stack.pop())
print("stack content: ",stack.items)
print("Top item: ",stack.top())
print("Stack is empthy: ",stack.is_empty())
print("stack size: ",stack.size())