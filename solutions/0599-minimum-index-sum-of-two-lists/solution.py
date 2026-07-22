class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        shortest = float('inf')
        res = []
        
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                index_sum = i + j
                
                if index_sum < shortest:
                    shortest = index_sum
                    res = [list1[i]] 
                elif index_sum == shortest:
                    res.append(list1[i]) 
                    
        return res

        
        # shortest=float('inf')
        # for i in range(len(list1)):
        #     if list1[i] in list2:
        #         shortest=min(shortest,i+list2.index(list1[i]))

        # res=[]
        # for i in range(len(list1)):
        #     if list1[i] in list2 and (i+list2.index(list1[i]))==shortest:
        #         res.append(list1[i])
        # return res
