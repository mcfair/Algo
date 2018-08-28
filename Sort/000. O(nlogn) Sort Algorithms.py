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
    i, j = 0, 0 #two pointer method
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

#Quick Sort is also a Divide and Conquer algorithm. 
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

#Heap Sort is an in-place sorting algorithm with worst case and average complexity of O(nlogn).

def heapify(arr, n, i):
    """ To heapify subtree rooted at index i. n is size of heap"""
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
        
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
