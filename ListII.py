lst = [23, 42, 108]

def append_size(lst):
  size: int=len(lst)
  return lst + [size]

print(append_size(lst))

#or

def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size(lst))
