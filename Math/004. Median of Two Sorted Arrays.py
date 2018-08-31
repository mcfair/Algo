class Solution(object):
    def findMedianSortedArrays(self, num1, num2):
        def kth(  k, s1, e1, s2, e2):
            #base cases
            if s1 == e1:
                return num2[s2+k]
            if s2 == e2:
                return num1[s1+k]
            if k == 0:
                return min(num1[s1], num2[s2])

            m = (e1+s1)/2
            n = (e2+s2)/2
            """
            visulization
            [s1    m][m+1  e1]
            [s2  n][n+1    e2]
            """
            #if k is more than the number of elements in left1 + left2
            #then we can exclude the smaller left half
            if (m-s1)+(n-s2) < k:
                if num1[m] < num2[n]:
                    return kth(k-(m-s1)-1, m+1, e1, s2, e2)
                else:
                    return kth(k-(n-s2)-1, s1, e1, n+1, e2)
            #if k is within the numbers of left1+left2
            #then we can exclude the larger right half
            else: 
                if num1[m] < num2[n]:
                    return kth(  k, s1, e1, s2, n)
                else:
                    return kth(  k, s1, m, s2, e2)

        M = len(num1)
        N = len(num2)
        L = M+N
        
        if L % 2 == 0:
            return 0.5*(kth( L/2-1, 0, M, 0, N) + kth(  L/2, 0, M, 0, N))
        return kth( L/2, 0, M, 0, N)
