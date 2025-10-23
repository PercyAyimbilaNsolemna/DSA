'''
    Problem: Valid Palindrome
    Takes 15 mins
    Hint



    Statement
    Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE.

    A phrase is considered a palindrome if it reads the same backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. Only alphanumeric characters (letters and digits) are taken into account.

    Constraints:

    1 ≤ 1≤ s.length ≤ 3000 ≤ 3000

    s consists only of printable ASCII characters.

    Time Complexit: O(n)
    Space Complexity: O(n)
'''

def is_palindrome(s):
    #Stores the start index in left and the last index in right
    left, right = 0, len(s) - 1

    #Loops through the array s
    while left < right:
        #Checks if s[left] is not a letter or number if yes it moves the left pointer one step
        while left < right and not s[left].isalnum():
            left += 1

        #Checks if s[right] is not a letter or number if yes it moves the right pointer one step
        while left < right and not s[right].isalnum():
            right -= 1

        #Converts letter on the left and right to lowercase and checks if they are not the same then we retuen False
        if s[left].lower() != s[right].lower():
            return False
            pass
        
        #Move the left pointer a step forward and the right pointer a step, backward
        left += 1
        right -= 1

    return True

def main():
    returnValue = is_palindrome('ka   Yak')
    if returnValue:
        print(f"\033[92m{returnValue}")
    else:
        print(f"\033[91m{returnValue}")


if __name__ == '__main__':
    main()
