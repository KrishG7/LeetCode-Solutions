class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        curr_line=[]
        curr_len=0

        for w in words:
            if curr_len+len(curr_line)+len(w)>maxWidth:
                res.append(self.format_line(curr_line, curr_len, maxWidth,False))
                curr_line,curr_len=[],0
            
            curr_line.append(w)
            curr_len+=len(w)

        res.append(self.format_line(curr_line, curr_len, maxWidth, True))
        return res

    def format_line(self, line, length, maxWidth, is_last):
    # If it's the last line or only one word, left-justify
        if is_last or len(line) == 1:
            return " ".join(line).ljust(maxWidth)
        
        # Calculate spaces to distribute
        total_spaces = maxWidth - length
        gaps = len(line) - 1
        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        # Build the line
        res = ""
        for i in range(gaps):
            res += line[i]
            # Add base spaces + one extra space if there's a remainder
            res += " " * (space_per_gap + (1 if i < extra_spaces else 0))
            
        return res + line[-1] # Add the last word
