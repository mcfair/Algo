#Iterative way - O(nlogn) - can use maxheap or simply sort

from collections import Counter
def leastInterval(self,tasks,n):

    q = sorted(Counter(tasks).values())

    maxInterval = q.pop()-1
    idleSlotes = n*maxInterval
    while q:
        idleSlotes -= min(q.pop(), maxInterval)

    return idleSlotes+len(tasks) if idleSlotes > 0 else len(tasks)    

        
#Math way - O(n) 

def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts)
    Msame = task_counts.count(M)
    return max(len(tasks), (M - 1) * (N + 1) + Msame)
