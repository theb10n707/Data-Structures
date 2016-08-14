def shellSort(list):
    print list
    space = len(list) // 2
    while space > 0:
        for startIndex in range(space):
            spaceInsertionSort(list, startIndex, space)
        space = space // 2
    print list

def spaceInsertionSort(list, startIndex, space):
    for num in range(startIndex+space, len(list), space):
        index = num
        currentValue = list[num]

        while currentValue < list[index-space] and index >= space:
            list[index] = list[index-space]
            index = index - space

        list[index] = currentValue

list = [6,3,6,9,4,2,1,5,8]
shellSort(list)
