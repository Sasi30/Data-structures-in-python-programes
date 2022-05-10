class stack:
    #create constructor
    def __init__(self):
     self.stack=list()
     self.maxsize=5
     self.top=0
    #insert an elements into the stack
    def push(self,data):
         if self.top>=self.maxsize:
           return "stack overflow"
         self.stack.append(data)
         self.top+=1
         return "element inserted"
    #delete an element from stack
    def pop(self):
        if self.top<=0:
            return"stack under flow"
        item=self.stack.pop()
        self.top-=1
        return item
    #size of stack
    def size(self):
        return self.top
s=stack()
print("push:",s.push(1))
print("push:",s.push(2))
print("push:",s.push(3))
print("push:",s.push(4))
print("push:",s.push(5))
print("push:",s.push(6))
print("size of stack:",s.size())
print("poped element:",s.pop())
print("poped element:",s.pop())
print("poped element:",s.pop())
print("poped element:",s.pop())
print("poped element:",s.pop())
print("poped element:",s.pop())
