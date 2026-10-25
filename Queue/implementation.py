class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def nq(self,item):
        self.items.append(item)
    def dq(self):
        if len(self.items)==0:
            return "Cannot pop,stack is empthy"
        return self.items.pop(0)
    def front(self):
         if len(self.items)==0:
                    return "Queue is empthy"
         return self.items[0]
    def rear(self):
             if len(self.items)==0:
                        return "Queue is empthy"
             return self.items[-1]
    def size(self):
         return len(self.items)
    
q=Queue()
q.nq(10)
q.nq(20)
q.nq(30)
print("Queue content: ",q.items)
print("Deque item: ",q.dq())
print("Queue content: ",q.items)
print("Front item: ",q.front())
print("Queue is empthy: ",q.is_empty())
print("Queue size: ",q.size())
print("Rare item: ",q.rear())