def arraySum(arr) :
  if arr == [] :
    return 0
  return arr[0] + arraySum(arr[1:])

print(arraySum([1, 2, 3]))