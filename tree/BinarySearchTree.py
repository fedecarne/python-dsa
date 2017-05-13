from collections import deque

class Node(object):

  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    
class BinarySearchTree(object):
  def __init__(self,root):
    self.root = Node(root)
      
  def insert(self,value):
    self.insert_helper(self.root,value)

  def insert_helper(self,start,value):
    if start is not None:
      if value<start.value:
        if start.left:
          self.insert_helper(start.left,value)
        else:
          start.left = Node(value)
      else:
        if start.right:
          self.insert_helper(start.right,value)
        else:
          start.right = Node(value)
  
  def search(self,value):
    return self.search_helper(self.root,value)
    
  def search_helper(self,start,value):
    
    if start is not None:
      if start.value == value:
        return True
      elif start.value<value:
        return self.search_helper(start.right,value)
      else:
        return self.search_helper(start.left,value)    
    else:
      return False
      
def tests():
  
  bst = BinarySearchTree(5)
  bst.insert(6)
  bst.insert(4)
  bst.insert(3)
  bst.insert(7)
  
  assert bst.root.left.left.value==3
  
  assert bst.search(3)==True
  assert bst.search(13)==False
  print "All tests passed :)"
  

if __name__ == '__main__':
  tests()        
      
