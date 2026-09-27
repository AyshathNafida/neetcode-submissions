class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=''.join(sorted(s))
        m=''.join(sorted(t))
        if n==m:
            return True
        else:
            return False
        