class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]] 
        """
        points =[]
        endsAt ={}
        for L, R, H in buildings:
            left, right = (L, 'left', -H), (R, 'right', -H) #'left' < 'right', don't use 'start' 'end'
            points += [left,right]
            endsAt[left] = right
        
        
        points = sorted(list(set(points))) #remove duplicates and sort
        rank = {points[i]: i for i in range(len(points))} # sorted index as rank
        tree = BIT(len(points))
        
        ret = []
        for p in points:
            if p[1] == 'left':
                q = endsAt[p]
                tree.update(rank[q], -p[-1]) # end idx is exclusive
            h = tree.query(rank[p]+1) # start idx is inclusive
            
            #not sure about this part!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if not ret or ret[-1][1] != h:
                if ret and ret[-1][0] == p[0]:
                    ret[-1][1] = h
                else:
                    ret.append([p[0], h])
        return ret
    
class BIT(object):
    def __init__(self, m):
        self.bit = [0] *(m+1)
    def update(self, p, h):
        while p > 0: # scope of h is towards left
            self.bit[p] = max(self.bit[p], h)
            p -= p & -p
    def query(self,p):
        ret = 0
        while p <= len(self.bit): # check anything to the right that has a higher value
            ret = max(ret, self.bit[p])
            p += p & -p
        return ret
