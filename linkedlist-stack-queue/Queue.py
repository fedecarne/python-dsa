class Empty(Exception):
  """Error attempting to access an element from an empty container."""
pass


class ArrayBasedQueue(object):
    def __init__(self,top=None):
      if top:
        self.data = [top]
      else:
        self.data = []
      
    def enqueue(self,value):
      self.data.append(value)
      
    def peek(self):
      return self.data[0]
      
    def dequeue(self):
      aux = self.data[0]
      self.data = self.data[1:]
      return aux
            


class Element(object):
    def __init__(self, value,next=None):
        self.value = value
        self.next = next

class LinkedQueue(object):

  def __init__(self):
    self.head = None
    self.tail = None
  
  def enqueue(self,item):    
    
    new_element = Element(item)
    if self.tail is not None:
      self.tail.next = new_element

    self.tail = new_element    
    
    if self.head is None:
      self.head = self.tail
  
  def dequeue(self):
    
    if not self.head:  
      raise Empty('Queue is empty')

    item, self.head = self.head, self.head.next 
    
    return item.value
      
      
def tests():
   
  q1 = ArrayBasedQueue()
  for i in range(4):
    q1.enqueue(i)

  for i in range(4):
    assert q1.dequeue()==i
  
  q2 = LinkedQueue()
  for i in range(4):
    q2.enqueue(i)

  for i in range(4):
    assert q2.dequeue()==i

  print 'All tests passed'

if __name__ == "__main__":
  tests()
