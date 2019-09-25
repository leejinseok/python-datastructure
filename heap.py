# 최소힙
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

  def get_left_child_idx(self, idx):
    return idx * 2
  
  def get_right_child_idx(self, idx):
    return idx * 2 + 1

  def is_go_up(self, idx, data):
    if idx <= 1:
      return False

    # 부모 인덱스의 값이 자식 인덱스의 값보다 크면 더 올라가 (최소힙)
    if self.arr[self.get_parent_idx(idx)] > self.arr[idx]:
      return True
    else:
      return False

  def is_go_down(self, idx, data):
    if self.len < self.get_left_child_idx(idx) or self.len < self.get_right_child_idx(idx): 
      return False
    
    left_child_data = self.arr[self.get_left_child_idx(idx)]
    right_child_data = self.arr[self.get_right_child_idx(idx)]

    print('left_child_data', left_child_data)
    print('right_child_data', right_child_data)

    if left_child_data < data or right_child_data < data:
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

  def delete(self):
    if self.is_empty():
      return None
    
    self.arr[1] = self.arr[self.len]
    self.arr.pop()
    self.len -= 1

    idx = 1
    data = self.arr[1]

    while self.is_go_down(idx, data):
      left_child_idx = self.get_left_child_idx(idx)
      right_child_idx = self.get_right_child_idx(idx)

      if data > self.arr[left_child_idx]:
        self.arr[idx] = self.arr[left_child_idx]
        idx = left_child_idx
      elif data > self.arr[right_child_idx]:
        self.arr[idx] = self.arr[right_child_idx]
        idx = right_child_idx

    self.arr[idx] = data
      
h = Heap()
h.insert(1)
h.insert(1)
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)
h.insert(7)
h.insert(8)
print(h.arr)

h.delete()

print(h.arr)
