class BinarySearchTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTreeNode(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTreeNode(value)
      else: 
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target > self.value:
        self.left = BinarySearchTreeNode(self.left)
        self.left.contains(target)
      else:
        self.right = BinarySearchTreeNode(self.right)
        self.right.contains(target)


  def get_max(self):
    if not self:
      return None
    if not self.right:
      return self.value
    return self.right.get_max()


  def for_each(self, cb):
    cd(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each