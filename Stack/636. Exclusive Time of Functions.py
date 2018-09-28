FET = collections.namedtuple('FunctionEventTime','fn,evt,time')
class Solution(object):
    def parselog(self,log):
        fn, evt, time = log.split(':')
        return FET(int(fn), evt, int(time))
        
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        time, stack = [0]*n, []
        recursivecalls = 0
        
        for log in logs:
            cur = self.parselog(log)
            
            if not stack or stack[-1].fn!=cur.fn or cur.evt=='start':
                stack.append(cur) 
                
            elif stack[-1].fn==cur.fn and cur.evt=='end' and stack[-1].evt=='start':
                start = stack.pop()
                time[cur.fn] += cur.time - start.time + 1  
                if stack:
                    time[stack[-1].fn] -=  cur.time - start.time +1
            
        return time
        
