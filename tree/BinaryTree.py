class TreeNode(object):
  """A node for the simple binary tree"""
  def __init__(self,value=None):
    
    self.value = value
    self.left = None
    self.right = None


class BinaryTree(object):
  """A simple binary tree"""
  
  def __init__(self,root=TreeNode()):
    self.root = root
      
  def add_left(self,parent,child):
  
    #validate that parent 
    if not isinstance(parent,TreeNode): 
      raise TypeError("parent must be proper TreeNode") 
    if parent.left is not None: 
      raise ValueError('Left child exists')
      
    parent.left = child
    
  def add_right(self,parent,child):
    
    if parent.right is not None: raise ValueError('Left child exists')
    parent.right = child
  
  def grow_from_list(self,input_list):
    """ Grow a tree from an list of elements."""
        
    self.root = TreeNode(input_list[0])    
    queue = [self.root]
    i=0
    while queue and i<len(input_list):
      node = queue.pop(0)
      i+=1
      if i<len(input_list):  
        node.left = TreeNode(input_list[i])
      i+=1
      if i<len(input_list):
        node.right = TreeNode(input_list[i])
      queue.extend([node.left,node.right])

  def pre_order_print(self):
    """ Print tree in pre-order"""    
    def pre_order_helper(node):
      if node:
        print node.value,
        pre_order_helper(node.left)
        pre_order_helper(node.right)
    
    pre_order_helper(self.root)  
    print ''  
      
  def in_order_print(self):        
    """ Print tree in in-order"""
    def in_order_helper(node):
      if node:
        in_order_helper(node.left)
        print node.value,
        in_order_helper(node.right)

    in_order_helper(self.root)  
    print ''  
      
  def post_order_print(self):    
    """ Print tree in post-order"""
    def post_order_helper(node):
      if node:
        post_order_helper(node.left)
        post_order_helper(node.right)
        print node.value,
      
    post_order_helper(self.root)  
    print ''  
      
  def bfs_print(self):  
      """ Print tree level by level"""

class tests():
  """Tests for BinaryTree"""
  
  root = TreeNode(1)
  tree1 = BinaryTree(root)
  tree1.add_left(tree1.root,TreeNode(2))
  tree1.add_right(tree1.root,TreeNode(3))
  
  assert tree1.root.value == 1
  assert tree1.root.left.value == 2
  assert tree1.root.right.value == 3
      
  tree2 = BinaryTree()
  tree2.grow_from_list([1,2,[],4,5])
  assert tree2.root.left.value == 2
  assert tree2.root.right.value == []
  assert tree2.root.left.left.value == 4
  assert tree2.root.left.right.value == 5
  
  tree2.pre_order_print()
  tree2.in_order_print()
  tree2.post_order_print()
  
  print "All tests passed"
  
  
if __name__ == "__main__":
  tests()  
      
  
