def merge(start, g, end, array):
    i = start
    j = g
    tp = []
    while i < g and j <= end:
        if array[i] < array[j]:
            tp.append(array[i])
            i += 1
        else:
            tp.append(array[j])
            j += 1
    while i < g:
        tp.append(array[i])
        i += 1
    while j <= end:
        tp.append(array[j])
        j += 1
    e = 0
    for i in range(start, end + 1):
        array[i] = tp[e]
        e += 1


def mergesort(left, right, array):  # lewy,prawy,tablica
    if left < right:
        middle = (left + right) // 2
        mergesort(left, middle, array)
        mergesort(middle + 1, right, array)
        merge(left, middle + 1, right, array)

arr = [45, 62, 21, 543, 23, 5254]
mergesort(0, 4, arr)
print(arr)
