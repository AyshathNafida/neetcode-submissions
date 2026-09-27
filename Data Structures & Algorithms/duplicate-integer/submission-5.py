class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m=[]
        for i in nums:
            if i not in m:
                m.append(i)
            else:
                return True
        else:
            return False
            