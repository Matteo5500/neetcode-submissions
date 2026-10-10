class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        gia_visti = set()
        for elemento in nums:
            if elemento in gia_visti:
                return True
            gia_visti.add(elemento)
            
        return False