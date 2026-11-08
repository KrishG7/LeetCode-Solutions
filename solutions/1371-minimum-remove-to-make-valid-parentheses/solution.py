class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        count=0
        for i in s:
            if i == '(':
                stack.append(i)
                count+=1
            elif i == ')':
                if count>=1:
                    stack.append(i)
                    count-=1
            else:
                stack.append(i)
        if count==0:
            return "".join(stack)
        else:
            res=[]
            for char in reversed(stack):
                if char =='(' and count>0:
                    count-=1
                else:
                    res.append(char)

        return "".join(reversed(res))
            
