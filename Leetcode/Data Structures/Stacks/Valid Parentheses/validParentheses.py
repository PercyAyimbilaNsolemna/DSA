'''
    https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    

    Example 1:

    Input: s = "()"
    Output: true
    Example 2:

    Input: s = "()[]{}"
    Output: true
    Example 3:

    Input: s = "(]"
    Output: false
    

    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Algorithm

        Loop through s and check if the top of the stack is the same as the same char then pop the char from thye stack
        If not push the char to the stack 

        '''
        #Creates a hash map that saves each parenthses and the opposite
        mapping = {'(': ')', '{': '}', '[': ']'}

        #Creates an empty stack
        stack = []

        #Loops through the string(s)
        for char in s:
            #Checks if the stack is not empty and the char at the top of the stack is the same as the current char
            if stack and mapping.get(stack[-1]) == char:
                #Reomves the char from the top of the stack
                stack.pop()
            #If the stack is not empty and the top char is not ythe same as the char, adds the char to the top of the stack
            else:
                stack.append(char)

        #Checks if the stack is not empty then it returns False
        if stack :
            return False
        
        #If not it returns True since the stack is empty
        return True


def main():
    solution = Solution()

    print(solution.isValid('()[]{}'))



if __name__ == '__main__':
    main()