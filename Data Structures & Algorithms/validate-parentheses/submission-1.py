class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                last_i=stack.pop()
                if i==')' and (last_i=='[' or last_i=='{') :
                    return False
                if i==']' and (last_i=='(' or last_i=='{') :
                    return False
                if i=='}' and (last_i=='[' or last_i=='(') :
                    return False
        return len(stack)==0
                    
        