#!/usr/bin/env python
# coding: utf-8

# In[17]:


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[min_idx], array[step]) = (array[step], array[min_idx])


data = [4,1,9,2,3,6]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)


# In[ ]:





# In[ ]:





# In[3]:


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
print("SS is :")
print(data)


# In[ ]:




