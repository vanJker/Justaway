class Solution:
    '''
    1. HashMap: $O(n)$ and $O(n)$
    Using hashmap to count numbers of each character in each string, then 
    compare these hashmaps.
    2. Sort: $O(nlogn)$ and $O(1)$
    ```
    return sorted(s) == sorted(t)
    ```
    dict.get: https://docs.python.org/3/library/stdtypes.html#dict.get
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        if len(countS) != len(countT):
            return False
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True