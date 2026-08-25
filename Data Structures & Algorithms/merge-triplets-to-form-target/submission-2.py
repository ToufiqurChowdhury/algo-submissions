class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        clen = len(triplets[0])
        triplet = [0] * clen
        
        for r in range(len(triplets)):
            if triplets[r][0] <= target[0] and triplets[r][1] <= target[1] and triplets[r][2] <= target[2]:
                for c in range(clen):
                    triplet[c] = max(triplet[c], triplets[r][c])

        return triplet == target
        