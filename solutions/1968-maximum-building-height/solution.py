class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Initialize dictionary: {building_id: max_height}
        # Start with the mandatory building 1 at height 0
        limits = {1: 0}
        for id, h in restrictions:
            limits[id] = h
            
        # 2. Get sorted IDs to "jump" across the city
        sorted_ids = sorted(limits.keys())
        
        # 3. Forward Pass: Propagate left-to-right
        for i in range(1, len(sorted_ids)):
            prev_id, curr_id = sorted_ids[i-1], sorted_ids[i]
            # Height cannot exceed prev + distance
            limits[curr_id] = min(limits[curr_id], limits[prev_id] + (curr_id - prev_id))
            
        # 4. Backward Pass: Propagate right-to-left
        # This is the "secret sauce" that allows the "future" 
        # restrictions to influence the "past" buildings.
        for i in range(len(sorted_ids) - 2, -1, -1):
            curr_id, next_id = sorted_ids[i], sorted_ids[i+1]
            # Height cannot exceed next + distance
            limits[curr_id] = min(limits[curr_id], limits[next_id] + (next_id - curr_id))
            
        # 5. Calculate the peak in the gaps
        ans = 0
        for i in range(len(sorted_ids) - 1):
            id1, h1 = sorted_ids[i], limits[sorted_ids[i]]
            id2, h2 = sorted_ids[i+1], limits[sorted_ids[i+1]]
            
            # The peak between two points (id1, h1) and (id2, h2)
            # The formula derives from the intersection of two lines:
            # y = h1 + (x - id1) and y = h2 + (id2 - x)
            peak = (h1 + h2 + id2 - id1) // 2
            ans = max(ans, peak)
            
        # 6. Final check: the gap after the last restriction to building n
        ans = max(ans, limits[sorted_ids[-1]] + (n - sorted_ids[-1]))
        
        return ans
