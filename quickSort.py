
def quickSort(list, start, end):
    if start >= end:
        return list

    pivot = start # choice
    #for insitu sort, swap pivot with end
    list[pivot],list[end] = list[end], list[pivot]
    comp = list[end] # val of pivot
    partition = start
    for i in range(start,end):
        if list[i] < comp:
            list[partition],list[i] = list[i],list[partition]
            partition += 1
    
    # if loop wont run for final element where list[i] = comp
    list[end],list[partition] = list[partition],list[end]
    # dont include partition in sub lists
    quickSort(list,start, partition-1)
    quickSort(list, partition+1, end)
        


list = [3,6,2,45,7,89,2,5]

quickSort(list, 0, len(list)-1)
print(list)