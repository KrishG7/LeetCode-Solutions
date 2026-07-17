class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        low = 0
        high = len(s_list) - 1
        vowels = set("aeiouAEIOU")
        
        while low < high:
            while low < high and s_list[low] not in vowels:
                low += 1
            while low < high and s_list[high] not in vowels:
                high -= 1
                
            s_list[low], s_list[high] = s_list[high], s_list[low]
            low += 1
            high -= 1
 
        return "".join(s_list)
