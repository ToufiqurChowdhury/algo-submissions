class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time | O(n) space

        complement_dict = {} # dict for nums and complement

        # iterate through the array
        for i, n in enumerate(nums):

            complement = target - n
            
            # check if complement in the dict
            if(complement in complement_dict):
                # if found in dict return index of the current number and the complement
                return [complement_dict[complement], i]
            else:
                # if not found then record the num and index in the dict
                complement_dict[n] = i

        return None