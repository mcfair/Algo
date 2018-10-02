
```
  def singleNumberOther3(nums):
    a = b = 0
    for num in nums:
        b = b ^ num & ~a
        a = a ^ num & ~b
    return a|b
```
