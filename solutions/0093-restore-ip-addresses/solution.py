class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        
        # Optimization: An IP address can't be shorter than 4 or longer than 12 digits
        if n < 4 or n > 12:
            return []

        def backtrack(start, path):
            # Base Case: Found 4 segments
            if len(path) == 4:
                if start == n:
                    res.append(".".join(path))
                return # Exit immediately!
            
            # Explore segment lengths 1, 2, 3
            for length in range(1, 4):
                if start + length > n:
                    break
                
                segment = s[start : start + length]
                
                # Pruning: Invalid segments (leading zeros or > 255)
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                path.append(segment)
                backtrack(start + length, path)
                path.pop() # Backtrack
                
        backtrack(0, [])
        return res
