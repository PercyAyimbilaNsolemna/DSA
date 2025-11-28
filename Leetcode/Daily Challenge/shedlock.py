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
        s = sorted(s)

        #Declares variables to hold the valid count, the left and the right variables counter
        leftCounter = 1
        rightCounter = 1

        #Valid count
        validCount = s.count(s[0])

        #Declares the left and right pointers
        leftPointer = 0
        rightPointer = len(s) - 1

        #Loops through the s(list) to check if the string satisfies the condition or not
        while leftPointer < rightPointer:
            """
                Pythonic
                    leftCounter = leftCounter + 1 if s[leftPointer] == s[leftPointer + 1] else 1
                
            """

            #Conditions that counts the same var on the left and checks if it is the same as the 
            #valid count
            if s[leftPointer] == s[leftPointer + 1]:
                leftCounter += 1
            else:
                print(f"------- {s[leftPointer]} : {leftCounter} --------\n")
                if leftCounter - 1 == 0 or leftCounter - 1 == validCount or leftCounter == validCount:
                    leftCounter = 1
                else:
                    return False

            #Condition that counts the same var on the right and checks if it is the same as the 
            #valid count
            if s[rightPointer] == s[rightPointer - 1]:
                rightCounter += 1
            else:
                print(f"------- {s[rightPointer]} : {rightCounter} --------\n")
                if rightCounter - 1 == 0 or rightCounter - 1 == validCount or rightCounter == validCount:
                    rightCounter = 1 
                else:  
                    return False

            leftPointer += 1
            rightPointer -= 1

        print(s)

        return True

def main():
    shedlock = Shedlock()
    print(shedlock.isValid("abccc"))


if __name__ == "__main__":
    main()