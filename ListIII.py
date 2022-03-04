lst=[1, 1, 2]

def append_sum(lst):
  lst.append(lst[-1]+lst[-2])
  lst.append(lst[-1]+lst[-2])
  lst.append(lst[-1]+lst[-2])
  return lst

print(append_sum(lst))

#or

def append_sum(lst):
  for append_sum in range(len(lst)): 
    lst.append(lst[-1]+lst[-2])
  return lst

print(append_sum(lst))
