class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None

  def is_empty(self):
    if not self.head:
      return True
    else:
      return False

  def push(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def pop(self):
    if self.is_empty():
      return None
    
    ret_data = self.head.data
    self.head = self.head.next
    return ret_data

  def peek(self):
    if self.is_empty():
      return None
    return self.head.data

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

while not s.is_empty():
  print(s.pop())