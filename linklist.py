class Node:
  def __init__(self,initval=None):
    self.value = initval
    self.next = None

  def isempty(self):
    return(self.value == None)

  def append(self,v):#append a value v
    if self.isempty():
      self.value = v
    elif self.next == None:
      newnode = Node(v)
      self.next = newnode
    else:
      self.next.append(v)
    return()

  def appendi(self,v):#append iteratively
    if self.isempty():
      self.value = v
      return()
    temp = self
    while temp.next != None:
      temp = temp.next
    newnoode = Node(v)
    temp.next = newnode

  def insert(self,v):#insert a value v
    if self.isempty():
      self.value = v
      return()
    newnode = Node(v)
    #exchange values in self and newnode
    (self.value, newnode.value) = (newnode.value,self.value)
    (self.next, newnode.next) = (newnode.next,self.next)

  def delete(self,x):#delete first value in list
    if self.isempty():
      return()
    if self.value == x: #value to be deleted is first value
      if self.next == None:
        self.value = None
      else:
        self.value = self.next.value
        self.next = self.next.next
        return()
    temp = self #first x to be deleted
    while temp.next != None:
      if temp.next.value == x:
        temp.next = temp.next.next
        return()
      else:
        temp = temp.next
    return()
  
  def delete_rec(self,x):#delete first value in list
    if self.isempty():
      return()
    if self.value == x: #value to be deleted is first value
      if self.next == None:
        self.value = None
      else:
        self.value = self.next.value
        self.next = self.next.next
        return()
    else:
      if self.next != None:
        self.next.delete(v)
        if self.next.value == None:
          self.next = self.next.next
    return()

  def __str__(self):
    selflist = []
    if self.value == None:
      return(str(selflist))
    temp = self
    selflist.append(temp.value)
    while temp.next != None:
      temp = temp.next
      selflist.append(temp.value)
    return(str(selflist))
    
