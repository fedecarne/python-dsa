class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
        
    def __init__(self, head=None):
        self.head = head
                        
    def append(self, value):
      
      current = self.head
      
      if self.head:      
        while current.next:
          current = current.next
        current.next = Element(value)
      else:
        self.head = Element(value)
        
    def print_list(self):
      
      current = self.head
      
      while current.next:
        print current.value,
        current = current.next
      print current.value
      
    def to_list(self):
      
      array = []
      current = self.head
      
      while current.next:
        array.append(current.value)
        current = current.next
      
      array.append(current.value)
      return array
                     
    def get_position(self,p):
      
      current = self.head
      
      for i in range(0,p):
        if current.next:
          current = current.next
        else:
          return 0
        
      return current.value         
     
    def insert(self,p,v):
         
      if p==0:
      
        self.head, self.head.next = Element(v), self.head
        
      else:
                     
        current = self.head

        for i in range(0,p-1):
          
          if current.next:
            current = current.next
          else:
            return
                
        temp = current.next
        current.next = Element(v)        
        current.next.next = temp 
                    
        return
     
    def delete(self,p):

      if p==0:      
        self.head = self.head.next
      
      else:
      
        current = self.head
                
        for i in range(p):
          if current.next:
            prev = current
            current = current.next          
          else:
            return

        prev.next = current.next
                 
      return
      
    def remove_dups(self):

      current = second = self.head
      while current is not None:
        while second.next is not None:
          if second.next.value == current.value:
            second.next = second.next.next
          else:
            second = second.next
        current = second = current.next      

    def remove_dupsdict(self):
        
        dups = {}
        current = self.head
        dups[self.head.value] = True
        while current.next is not None:
          if dups.has_key(current.next.value):
            if current.next.next is not None:
              current.next = current.next.next
            else:
              current.next = None
          else:
            dups[current.next.value] = True
            current = current.next                  
            
    def reverse(self):
      
      current = self.head
      
      size=0
      while current.next:
        current = current.next
        size+=1
      size+=1
      
      for i in range(self.size()): 
      
        current = self.head
        while current.next:
          current = current.next
        self.delete(size-1)
        self.insert(i,current.value)
      return
        
    def reverse_pro(self):
    
      prevNode = []
      nextNode = []
      current = self.head          
      while current:
          nextNode = current.next
          current.next = prevNode         
          prevNode = current
          current = nextNode
          
      self.head = prevNode          


    def get_k_to_last(self,k):
    
      Node1 = self.head
      Node2 = self.head
      
      for i in range(k):
        Node1 = Node1.next
      
      while Node1.next:
          Node1 = Node1.next
          Node2 = Node2.next   

      return Node2.value
    
    def size(self):
      return self.size_helper(self.head)
            
    def size_helper(self,node):
      if node.next:
        return 1+self.size_helper(node.next)
      else:
        return 1;
          
      return 
     
 
def test():
  ll = LinkedList()
  ll.append(1)
  assert ll.head.value == 1 # [1]
 
  ll.append(2)#[1,2]
  assert ll.head.next.value == 2 

  assert ll.get_position(0)==1
  assert ll.get_position(1)==2

  ll.insert(1,3)

  assert ll.to_list() == [1,3,2]

  assert ll.get_position(2)==2
  
  ll.append(4)
  ll.append(5)
  ll.append(6)

  assert ll.to_list() == [1,3,2,4,5,6]
  assert ll.get_position(4)==5
  ll.delete(4)
  assert ll.to_list() == [1,3,2,4,6]
  assert ll.get_position(4)==6
  
  ll.append(33)
  ll.append(33)
  assert ll.get_position(5)==ll.get_position(6)
  ll.remove_dups()
  assert ll.to_list() == [1,3,2,4,6,33]
  
  ll.append(33)
  assert ll.to_list() == [1,3,2,4,6,33,33]
  ll.remove_dupsdict()
  assert ll.to_list() == [1,3,2,4,6,33]
    
  ll.reverse()
  assert ll.to_list() == [33,6,4,2,3,1]
    
  assert ll.size() == 6

  ll.reverse_pro()
  assert ll.to_list() == [1,3,2,4,6,33]

  assert ll.get_k_to_last(4)==3
    
  print "All tests passed"
      
if __name__ == "__main__":
  test()      
