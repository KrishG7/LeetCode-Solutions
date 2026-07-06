class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # First sort by x[0], if ties use -x[1] so it sorts descending
        intervals.sort(key=lambda x:(x[0],-x[1]))
        
        valid_intervals=0
        max_end_seen=-1

        for start,end in intervals:
            if end>max_end_seen:
                valid_intervals+=1
                max_end_seen=end
        
        return valid_intervals
