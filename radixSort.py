def radix_sort(list):
 
  maxExp = len(str(max(list)))
  buildList = list[:]

  for exponent in range(maxExp):

    expBins = [[] for i in range(10)]

    for number in buildList:
      numberStr = str(number)
      try:
        digit = numberStr[-(exponent + 1)]
      except IndexError:    # put all shorter numbers in 0 bin (they are already in order)
        digit = 0
        
      digit = int(digit)

      expBins[digit].append(number)

    buildList = []
    for expBin in expBins:
      buildList.extend(expBin)

  return buildList

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print(radix_sort(unsorted_list))