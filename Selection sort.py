

def selectionSort(array,size):
    for i in range(size):
        min_index = i
        
        for j in range(i+1,size):
            if array[j] < array[min_index]:
                min_index = j
        
        (array[i],array[min_index]) = (array[min_index],array[i])


data = [2,9,4,6,9,5]
size = len(data)
selectionSort(data,size)
print("Selection sort is :")
print(data)





