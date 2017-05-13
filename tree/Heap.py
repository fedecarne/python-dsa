class Item(object):
  def __init__(self,key,value):
    self.key = key
    self.value = value
    

class ArrayBasedHeap(object):
  def __init__(self):
    self.data = []
    
  def print_heap(self):
    print [x.value for x in self.data] 
      
  def parent(self,j):
    return (j-1)//2

  def left(self, j):
    return 2*j + 1
  
  def right(self, j):
    return 2*j + 2

  def has_left(self, j):
    return self.left(j) < len(self.data)

  def has_right(self, j):
    return self.right(j) < len(self.data)
    
  def swap(self, i,j):
    self.data[i], self.data[j] = self.data[j], self.data[i]
          
  def upheap(self,j):
    parent = self.parent(j)
    if j>0 and self.data[j].key<self.data[parent].key:
      self.swap(j,parent)
      self.upheap(parent)
  
  def add(self,key,value):
    self.data.append(Item(key,value))
    self.upheap(len(self.data)-1) 
    
  def pop_min(self):
    self.swap(0,len(self.data)-1)
    item = self.data.pop()
    self.downheap(0)
    return (item.key,item.value)
    
  def downheap(self,j):
    if self.has_left(j):
      left = self.has_left(j) 
      small_child = left
      if self.has_right(j):
        right = self.has_right(j)
        if self.data[right].key<self.data[left].key:
          small_child = right
          
      if self.data[small_child].key< self.data[j].key:
        self.swap(small_child,j)
        self.downheap(small_child)

def test():
  
  h = ArrayBasedHeap()

  h.add(7,'A')
  h.add(17,'B')
  h.add(10,'C')
  h.add(15,'P')
  
  h.print_heap()
  
  x = h.pop_min()
  assert x[0] == 7
  assert x[1] == 'A'

  print 'All tests passed :)'
  
if __name__ == '__main__':
  test()  
