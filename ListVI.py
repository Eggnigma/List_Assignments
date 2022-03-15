def combine_sort(lst1,lst2):
  combine = lst1 + lst2
  sorted_list = sorted(combine)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
