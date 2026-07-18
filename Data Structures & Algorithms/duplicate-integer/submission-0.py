class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) time | O(n) space
        
        duplicates = set()

        for num in nums:
            if num in duplicates:
                return True
            duplicates.add(num)
        return False