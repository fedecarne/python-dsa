class Empty(Exception):
  """Error attempting to access an element from an empty container."""
pass

class Element(object):
    def __init__(self, value,next):
        self.value = value
        self.next = next

class Stack():

  def __init__(self):
    self.head = None
  
  def push(self,item):    

    self.head = Element(item,self.head)
  
  def pop(self):
    
    if not self.head:  
      raise Empty('Stack is empty')

    item, self.head = self.head, self.head.next 
    
    return item.value
    
def tests():
  
  stack = Stack()
  for i in range(4):
    stack.push(i)

  poplist = []  
  for i in range(4):
    poplist.append(stack.pop())
  
  assert poplist == [3,2,1,0]
  stack.pop()      
  print "All tests passed :)"

if __name__=='__main__':
  tests()  
