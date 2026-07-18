class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Algo: Bin Search
        # TC: O(logn)
        # SC: O(1)
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            lookup = target-numbers[i]
            while l<=r:
                mid = l + (r-l) // 2
                if numbers[mid] == lookup:
                    return [i+1, mid+1]
                elif numbers[mid] < lookup:
                    l = mid+1
                else:
                    r = mid-1