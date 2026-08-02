class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cite = sorted(citations, reverse=True)
        i = 0
        while i < len(cite) and cite[i] >= i + 1:
            i += 1
        return i

