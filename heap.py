class Heap:
  def __init__(self):
    self.arr = [None, ]
    self.len = 0

  def is_empty(self):
    if self.len == 0:
      return True
    else:
      return False

  def get_parent_idx(self, idx):
    return idx // 2

  def is_go_up(self, idx, data):
    if idx <= 1:
      return False

    # 부모 인덱스의 값이 자식 인덱스의 값보다 크면 더 올라가 (최소힙)
    if self.arr[self.get_parent_idx(idx)] > self.arr[idx]:
      return True
    else:
      return False

  def insert(self, data):
    if self.is_empty():
      self.arr.append(data)
      self.len += 1
      return

    self.arr.append(data)
    self.len += 1

    idx = self.len

    while self.is_go_up(idx, data):
      parent_idx = self.get_parent_idx(idx)
      self.arr[idx] = self.arr[parent_idx]
      idx = parent_idx
    
    self.arr[idx] = data

h = Heap()
h.insert(3)
h.insert(1)
h.insert(2)

print(h.arr)
