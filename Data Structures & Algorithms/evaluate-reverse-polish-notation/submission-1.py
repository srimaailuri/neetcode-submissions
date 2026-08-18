class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=["+","-","*","/"]
        for i in tokens:
            if i == "+":
                b=stack.pop()
                a=stack.pop()
                result=a+b
                stack.append(result)
            elif i == "-":
                b=stack.pop()
                a=stack.pop()
                result=a-b
                stack.append(result)
            elif i == "*":
                b=stack.pop()
                a=stack.pop()
                result=a*b 
                stack.append(result) 
            elif i == "/":
                b=stack.pop()
                a=stack.pop()
                result=int(a/b)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[-1]


        