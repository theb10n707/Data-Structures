def selectionSort(list):
    print list
    length = len(list) - 1
    for times in range(0,length):
        minNum = list.index(min(list[times:]))
        temp = list[minNum]
        list[minNum] = list[times]
        list[times] = temp
    print list

list = [6,3,6,9,4,2,1,5,8]
selectionSort(list)