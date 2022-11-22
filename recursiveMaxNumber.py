def recursiveMax(arr) :
  if len(arr) == 1 :
    return arr[0]
  sub_max = recursiveMax(arr[1:])
  return sub_max if sub_max > arr[0] else arr[0]

print(recursiveMax([2]))