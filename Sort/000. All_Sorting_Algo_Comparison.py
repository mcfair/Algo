#Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, 
#calls itself for the two halves and then merges the two sorted halves.
#O(nlogn)
def merge_sort(m):
    if len(m) <= 1:
        return m
  
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
  
    left = merge_sort(left)
    right = merge_sort(right)
    
    return list(heapq.merge(left, right))
    #heapq.merge is used to merge two sorted array, or use the function below
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
#Quick Sort is a Divide and Conquer algorithm. 
#It picks an element as pivot and partitions the given array around the picked pivot.
#There are different ways of picking pivot: always first item, always last item, random item, or median
#O(nlogn) - Note the implementation below is not in-place.
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    less, more , pivotList  = [], [], []
 
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            pivotList.append(i)
    less = quickSort(less)
    more = quickSort(more)
    return less + pivotList + more
    
#=================================== Inefficient O^2 sort algorithms ======================================#

#Bubble Sort works by repeatedly swapping the adjacent elements if they are in wrong order.
#O(n^2)
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
            
#Insertion sort works the way we sort playing cards in our hands, moving elements one at a time to the correct position.
#O(n^2)
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
    
        j = i-1
        while j >=0 and arr[j] > key :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

#Selection sort repeatedly finds the minimum element from unsorted part and put it at the beginning.    
#It's more like a reverse process of bubble sort
#O(n^2)
def selectionSort(A):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the index of minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with the current element        
        A[i], A[min_idx] = A[min_idx], A[i]
