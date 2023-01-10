def merge_sort(myList):
  if len(myList) <= 1:
    return myList

  mid = len(myList) // 2
  leftBranch = myList[:mid]
  rightBranch = myList[mid:]

  leftSorted = merge_sort(leftBranch)
  rightSorted = merge_sort(rightBranch)

  return merge(leftSorted, rightSorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

nums = [5,2,7,5,2,8,2,9]

print(merge_sort(nums))
