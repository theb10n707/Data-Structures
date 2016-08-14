def quickSort(list):
    print list
    quickSortDriver(list, 0, len(list)-1)

def quickSortDriver(list,first,last):
    if first < last:
        middle = partition(list, first, last)

        quickSortDriver(list, first, middle-1)
        quickSortDriver(list, middle+1, last)
    print list

def partition(list,first,last):
    pivot = list[first]
    leftMark = first + 1
    rightMark = last
    good = False

    while not good:
        while leftMark <= rightMark and list[leftMark] <= pivot:
            leftMark = leftMark + 1

        while list[rightMark] >= pivot and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            good = True

        else:
            temp = list[leftMark]
            list[leftMark] = list[rightMark]
            list[rightMark] = temp

    temp = list[first]
    list[first] = list[rightMark]
    list[rightMark] = temp

    return rightMark

list = [6,3,6,9,4,2,1,5,8]
quickSort(list)