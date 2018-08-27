The Merge Sort use the Divide-and-Conquer approach to solve the sorting problem. 
First, it divides the input in half using recursion. 
After dividing, it sort the halfs and merge them into one sorted output.


```
# C = output [length = N]
# A 1st sorted half [N/2]
# B 2nd sorted half [N/2]
i = j = 1
for k = 1 to n
    if A[i] < B[j]
        C[k] = A[i]
        i++
    else
        C[k] = B[j]
        j++
```


https://www.youtube.com/watch?v=Pr2Jf83_kG0
