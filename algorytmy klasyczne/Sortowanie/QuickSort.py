def qsort(left, right, array):
    middle = array[(right + left) // 2]
    leftLoop = left
    rightLoop = right

    while leftLoop < rightLoop:
        while array[leftLoop] < middle:
            leftLoop += 1
        while array[rightLoop] > middle:
            rightLoop -= 1
        if leftLoop <= rightLoop:
            array[leftLoop], array[rightLoop] = array[rightLoop], array[leftLoop]
            leftLoop += 1
            rightLoop -= 1
       # print(array)
    if left < rightLoop:
        qsort(left, rightLoop, array)
    if leftLoop < right:
        qsort(leftLoop, right, array)