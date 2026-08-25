class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        clen = len(triplets[0])
        triplet = [0] * clen
        
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                col = 0
                while col < clen:
                    triplet[col] = max(triplet[col], triplets[i][col])
                    col += 1

        return triplet == target
        