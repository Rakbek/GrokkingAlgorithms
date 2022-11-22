def numberOfElements(arr) :
  if arr == [] :
    return 0
  return 1 + numberOfElements(arr[1:])

print(numberOfElements([1, 2, 3, 4, 6, 7]))