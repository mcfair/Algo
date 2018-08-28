#Counting Sort O(n+k)
#n is the number of elements, k is the length of range
"""
Counting Sort works for arrays with finite known range, i.e. human ages (0~120), alphabets (a~z), etc.
Simply count the occurance of each item, then reconstruct the array in order.
This method is useful only when O(k)~=O(n)
When O(k) is asymptotically greater than O(nlogn), use Radix Sort.
"""

#Radix Sort
def radix_sort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
        
def countingSort(arr, exp1):
    """A function to do counting sort of arr[] according to the digit represented by exp."""
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * n
 
    # count stores the occurence of each digit 0~9
    count = [0] * 10
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        digit = (arr[i]/exp1)
        count[ (digit)%10 ] += 1
 
    # Cumulate count[i] so that count[i] becomes the the position of digit i in output array
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
