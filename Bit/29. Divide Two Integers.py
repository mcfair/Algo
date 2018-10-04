"""
Divide a by b, without using multiplication, division and mod operators.
Which means we can only use +, -, and bit operations.
"""
#O(logN^2) - This method practically uses larger than 32 bit (but Python has no int type constraint)
def divide(self, a, b):
    negative = (a < 0) ^ (b < 0) 
    a, b, res = abs(a), abs(b), 0
    while a >= b:
        i = 0                     #i can only be power of 2
        while a >= b << (i + 1): 
            i += 1                #find max i such that a = 2^i * b + c                       
        res += 1 << i             #update the quotient with highest bit
        a -= b << i               #decrease a = a - b*2^i
    return min(-res if negative else res, 2147483647)

# O(32) - This is a real 32bit implementation
def divide(self, A, B):
    if (A == -2147483648 and B == -1): #handle overflow in 32bit enviroment
        return 2147483647 
    a, b, res = abs(A), abs(B), 0
    for i in range(32)[::-1]:          #try bit by bit from high bit to low bit
        if (a >> i) - b >= 0:
            res += 1 << i
            a -= b << i
    return -res if (A > 0)^(B > 0) else res
"""
In this problem, we are asked to divide two integers. However, we are not allowed to use division, multiplication and mod operations. So, what else can we use? Yeah, bit manipulations.

Let's do an example and see how bit manipulations work.

Suppose we want to divide 15 by 3, so 15 is dividend and 3 is divisor. Well, division simply requires us to find how many times we can subtract the divisor from the the dividend without making the dividend negative.

Let's get started. We subtract 3 from 15 and we get 12, which is positive. Let's try to subtract more. Well, we shift 3 to the left by 1 bit and we get 6. Subtracting 6 from 15 still gives a positive result. Well, we shift again and get 12. We subtract 12 from 15 and it is still positive. We shift again, obtaining 24 and we know we can at most subtract 12. Well, since 12 is obtained by shifting 3 to left twice, we know it is 4 times of 3. How do we obtain this 4? Well, we start from 1 and shift it to left twice at the same time. We add 4 to an answer (initialized to be 0). In fact, the above process is like 15 = 3 * 4 + 3. We now get part of the quotient (4), with a remainder 3.

Then we repeat the above process again. We subtract divisor = 3 from the remaining dividend = 3 and obtain 0. We know we are done. No shift happens, so we simply add 1 << 0 to the answer.

Now we have the full algorithm to perform division.

According to the problem statement, we need to handle some exceptions, such as overflow.

Well, two cases may cause overflow:

divisor = 0;
dividend = INT_MIN and divisor = -1 (because abs(INT_MIN) = INT_MAX + 1).
Of course, we also need to take the sign into considerations, which is relatively easy.

Putting all these together, we have the following code.
"""
