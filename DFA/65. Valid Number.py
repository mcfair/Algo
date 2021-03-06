class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        #define a DFA
        state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4},  #state 1
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},  #state 5
              {'sign':7, 'digit':8},          #state 6
              {'digit':8},                    #state 7
              {'digit':8, 'blank':9},         #state 8
              {'blank':9}]                    #state 9
        
        currentState = 1
        for c in s:
            if c in '0123456789':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in '+-':
                c = 'sign'
            if c not in state[currentState]:
                return False
            currentState = state[currentState][c]
             
        if currentState not in [3,5,8,9]:
            return False
        
        return True
