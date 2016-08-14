def insertionSort(list):
    print list
    for num in range(1, len(list)):
        index = num
        currentValue = list[num]

        while currentValue < list[index-1] and index > 0:
            list[index] = list[index-1]
            index = index - 1

        list[index] = currentValue

    print list

list = [6,3,6,9,4,2,1,5,8]
insertionSort(list)