class Heap:
  def __init__(self, lambda x,y : x>y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size)

  def delete(self):
    self.storage.pop()
    self._bubble_up(self.get_size)
    return self.get_size()

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      #compare to parent
      parent = (index -1)//2
      
      if self.storage[index] > self.storage[parent]:
        self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
        index = parent
      else: 
        break


  def _sift_down(self, index):
    left = (index * 2) + 2
    right = (index * 2) + 1
    parent = index #this is the node we need to target

    if parent < left:
      parent = left
    if parent < right:
      parent = right
    if parent != index:
      self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
      self._sift_down()
    #runs recuervly