class Heap:
  def __init__(self, comparator=lambda x,y : x>y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage) - 1
    self._bubble_up(index)

  def delete(self):
    if len(self.storage) == 0:
      return None
    deleted = self.storage[0]
    if len(self.storage) == 1:
      self.storage.pop()
    else:
      # swap max with last element, then remove it
      self.storage[0], self.storage[len(self.storage)-1] = self.storage[len(self.storage)-1], self.storage[0]
      self.storage.pop()
      self._sift_down(0)
    
      return deleted

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)
  
  def get_max(self):
    return self.storage[0]

  def _bubble_up(self, index):
    parent = (index - 1) // 2
    if index <= 0:
      return
    elif self.storage[parent] < self.storage[index]:
      self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      self._bubble_up(parent)


  # def _sift_down(self, index):
  #   left = (index * 2) + 2
  #   right = (index * 2) + 1
  #   parent = index #this is the node we need to target
  #   if left or right is None:
  #     return False
  #   else:
  #     if parent < left:
  #       parent = left
  #     if parent < right:
  #       parent = right
  #     if parent != index:
  #       self.storage[index] , self.storage[parent] = self.storage[parent] , self.storage[index]
  #       self._sift_down()
  #   #runs recuervly

  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    max = index
    if len(self.storage) > left and self.storage[max] < self.storage[left]:
      max = left
    if len(self.storage) > right and self.storage[max] < self.storage[right]:
      max = right
    if max == index:
     return
    else:
      self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
      self._sift_down(max)