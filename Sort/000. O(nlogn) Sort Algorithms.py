#Heap Sort is an in-place sorting algorithm using heap/priority queue.
#The implementation uses Python built-in min heap to demonstrate the idea.
#O(nlogn) - worst case and average complexity 
import heapq
def heap_sort(h):
    h = heapq.heapify(h)
    return [heapq.heappop(h) for i in range(len(h))]

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
def quick_sort(arr):
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


