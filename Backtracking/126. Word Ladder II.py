class Solution:
# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return a list of lists of string
    def findLadders(self, start, end, dic):
        dic = set(dic)
        if end not in dic: return []
        
        
        parents = collections.defaultdict(set)
        level = {start}
        #use bfs to gaurantee shortest distance
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(node)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
             
        #at this point, we created a parent hashtable
     
        #backtrack path (another BFS)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res
