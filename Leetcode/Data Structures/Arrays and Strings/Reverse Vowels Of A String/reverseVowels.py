'''
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

    Example 1:

    Input: s = "hello"
    Output: "holle"
    Example 2:

    Input: s = "leetcode"
    Output: "leotcede"
    

    Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o','u']
        indexMin = 0
        indexMax = len(s) - 1

        stringList = list(s)

        while indexMin < indexMax:
            if stringList[indexMin].lower() in vowels and stringList[indexMax].lower() in vowels:
                stringList[indexMin], stringList[indexMax] = stringList[indexMax], stringList[indexMin]
                indexMin += 1
                indexMax -= 1
            elif stringList[indexMin].lower() in vowels:
                indexMax -= 1
            elif stringList[indexMax].lower() in vowels:
                indexMin += 1
            else:
                indexMin += 1
                indexMax -= 1
        return ''.join(stringList) 

def main():
    solution = Solution()

    print(solution.reverseVowels("leetcode"))


if __name__ == '__main__':
    main()