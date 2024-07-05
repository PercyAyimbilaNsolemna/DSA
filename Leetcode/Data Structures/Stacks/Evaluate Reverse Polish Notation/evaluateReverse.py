'''
    https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

    150. Evaluate Reverse Polish Notation

    Medium
    Topics
    Companies
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
    

    Example 1:

    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    Example 2:

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

    Example 3:

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    

    Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

'''
from operator import add, sub, mul, truediv

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #Creates a dictionary that saves all the operators with their corresponding operations
        opeartors = {'+': add, '-': sub, '*': mul, '/': truediv }

        #Creates an empty stack to store the numbers
        stack = []


        for token in tokens:
            #Checks if the token is not an operator, then it adds it to the end of the stack
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(token)
            #If the token is an operator, the two recent tokens are pulled and the operation is performed on them
            else:
                #Pops the topmost token and puts it in num2
                num2 = int(stack.pop())
                #Pops the second topmost and puts it in num1 since that number came in to the stack before the current rear
                num1 = int(stack.pop())
                #Extracts the appropriate operation to be performed on the numbers from the opeartions dictionary
                answer = opeartors[token](num1, num2)
                print(f'{num1} {token} {num2} = {answer}')
                #Adds the answer to the stack
                stack.append(answer)
        return int(stack[-1])
            

    def checker(self, arrs):
        for arr in arrs:
            if arr != "+" and arr != "-" and arr != "*" and arr != "/":
                print(arr)
        print('Done!')


def main():
    solution = Solution()
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    #solution.checker(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])


if __name__ == '__main__':
    main()