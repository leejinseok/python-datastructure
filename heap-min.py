class Heap:
  def __init__(self):
    self.arr = []
    self.len = 0

  def get_parent_idx(self, idx):
    return idx // 2

  def is_go_up(self, idx):
    if idx < 1:
      return False
    
    parent_idx = self.get_parent_idx(idx)
    if self.arr[parent_idx] > self.arr[idx]:
      return True
    else:
      return False

  def insert(self, data):
    if self.len == 0:
      self.arr.append(data)
      self.len += 1
      return
    
    self.arr.append(data)
    self.len += 1
    idx = self.len - 1
    while self.is_go_up(idx):
      parent_idx = self.get_parent_idx(idx)
      self.arr[idx] = self.arr[parent_idx]
      idx = parent_idx

    self.arr[idx] = data

  def delete(self):
    if self.len == 0:
      return
    
    last_idx = self.len - 1
    ret = self.arr[last_idx]
    self.arr[0] = ret
    self.arr.pop()

h = Heap()
h.insert(1)
h.insert(3)
h.insert(4)
h.insert(2)

print(h.arr, h.len)

h.delete()
print(h.arr, h.len)