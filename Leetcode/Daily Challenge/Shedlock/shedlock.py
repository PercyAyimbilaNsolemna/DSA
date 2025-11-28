"""
    Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

    Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

    Example

    This is a valid string because frequencies are .


    This is a valid string because we can remove one  and have  of each character in the remaining string.


    This string is not valid as we can only remove  occurrence of . That leaves character frequencies of .

    Function Description

    Complete the isValid function in the editor below.

    isValid has the following parameter(s):

    string s: a string
    Returns

    string: either YES or NO
    Input Format

    A single string .

    Constraints

    Thought Process

    Firsly perform an inplace sorting to the string

    First Condition

    Use two pointers

    Declare  a variable to hold static count after the first iteration

    Starting counting from left and right

    If you hit a different variable check if the count is the same

        TODO:
            Complete this before close of week

"""

class Shedlock:
    def isValid(self, s):
        """
            Returns a boolean whether the given string satisfies the given conditions or not

        """

        #Sort the string inplace
        s.sort()
        validCount = 0
        leftCounter = 0
        rightCounter = 0

        return s

def main():
    shedlock = Shedlock()
    print(shedlock.isValid("Percy"))


if __name__ == "__main__":
    main()