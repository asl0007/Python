class Tree:
  def __init__(self, initval=None):
    self.value = initval
    if self.value:
      self.left = Tree()
      self.right = Tree()
    else:
      self.left = None
      self.right = None
    return
  
  def isempty(self):
    return(self.value == None)

  def isleaf(self):
    return(self.left.isempty() and self.right.isempty())

  def makeempty(self):#convert leaf to empty node
    self.value = None
    self.left = None
    self.right = None
    return

  def copyright(self):
    self.value = self.right.value
    self.left = self.right.left
    self.right = self.right.right
    return

  def find(self,v):#find a value v
    if self.isempty():
      return(False)
    if self.value == v:
      return(True)
    if v < self.value:
      return(self.left.find())
    else:
      return(self.right.find())
  
  def minval(self):#find minimum value i.e. leftmost node 
    #Assume tree is not empty
    if self.left == None:
      return(self.value)
    else:
      return(self.left.minval())
  
  def maxval(self):#find maximum value i.e. rightmost node 
    #Assume tree is not empty
    if self.right == None:
      return(self.value)
    else:
      return(self.right.minval())

  def insert(self,v):
    if self.isempty():#add v as a new leaf 
      self.value = v
      self.left = Tree()
      self.right = Tree()
    if self.value == v:#value is already present,do nothing
      return
    if v < self.value:
      self.left.insert(v)
      return
    if v > self.value:
      self.right.insert(v)
      return
  
  def delete(self,v):
    if self.isempty():
      return
    if v < self.value:
      self.left.delete(v)
      return
    if v > self.value:
      self.right.delete(v)
      return
    if v == self.value:
      if self.isleaf():
        self.makeempty()
      elif self.left.isempty():
        self.copyright()
      else:
        self.value = self.left.maxval()
        self.left.delete(self.left.maxval())
      return

  def inorder(self):#inorder traversal
    if self.isempty():
      return([])
    else:
      return(self.left.inorder() + [self.value] + self.right.inorder()) 

  def __str__(self):
    return(str(self.inorder()))
  

