'''
    Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        index_small = 0
        index_high = len(s) - 1

        while index_small < index_high:
            s[index_small], s[index_high] = s[index_high], s[index_small]
            index_small += 1
            index_high -= 1
        
        return s
        '''
        reversed_string = []

        for i in reversed(range(len(s))):
            reversed_string.append(s[i])

        return reversed_string
        '''
def main():
    solution = Solution()

    print(solution.reverseString(["H","a","n","n","a","h"]))


if __name__ == '__main__':
    main()       