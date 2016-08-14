def mergeSort(list):
    print list
    if len(list) > 1:
        length = len(list)//2
        leftHalf = list[:length]
        rightHalf = list[length:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        a,b,c = 0,0,0

        while a < len(leftHalf) and b < len(rightHalf):
            if leftHalf[a] < rightHalf[b]:
                list[c] = leftHalf[a]
                a = a + 1
            else:
                list[c] = rightHalf[b]
                b = b + 1
            c = c + 1

        while a < len(leftHalf):
            list[c] = leftHalf[a]
            a = a + 1
            c = c + 1

        while b < len(rightHalf):
            list[c] = rightHalf[b]
            b = b + 1
            c = c + 1

    print list

list = [6,3,6,9,4,2,1,5,8]
mergeSort(list)
