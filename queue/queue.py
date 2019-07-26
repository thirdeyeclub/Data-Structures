class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.size += 1
    self.storage.append(item)
    print("Que'd")
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop(0)
      print("DeQue'd", self.storage.pop(0))
    else:
      return None

  def len(self):
    return self.size
