class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    # 02d is a format specifier, 2 tells min width, d is decimal and 0 means fill empty with 0 (padding char)
                    res.append(f"{h}:{m:02d}")

        return res

