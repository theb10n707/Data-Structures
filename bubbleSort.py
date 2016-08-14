def bubbleSort(list):
    print list
    good = False
    while good != True:
        length = len(list) - 1
        for times in range(0, length):
            count = 0
            for number in range(0,length):
                a = list[number]
                b = list[number+1]
                if b > a:
                    temp = list[number]
                    list[number] = list[number+1]
                    list[number+1] = temp
                else:
                    count = count + 1
            if count == length:
                good = True
                break
    print list

list = [6,3,6,9,4,2,1,5,8]
bubbleSort(list)



