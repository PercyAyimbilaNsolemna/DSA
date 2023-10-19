'''
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    
    Example 1
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

    example 2
    Input: nums = [1,0,1,1,0,1]
    Output: 2
    
    Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    
'''

'''
    Declare two variables,
    One to hold the greatest consecutive ones and the other to count the number of ones
    If a zero or any other number apart from 1 is encountered, compare the number of ones in the variable 
    holding the greatest number of ones with the current number of ones counted
    If the current number of is greater than the previous then change the value of the variable holding the 
    greatest number of ones to the new counted ones else leave it as it is
    
'''

class Solution(object):
    def FindMaxConsecutiveOnes(self, nums):
        countOnes = 0
        greatestOnesCounted = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                countOnes += 1
                if index == len(nums) - 1:
                    if countOnes > greatestOnesCounted:
                        greatestOnesCounted = countOnes                   
            else:
                if countOnes > greatestOnesCounted:
                    greatestOnesCounted = countOnes
                countOnes = 0
        return f'The greatest consecutive ones counted is {greatestOnesCounted}'

    
def main():
    solution = Solution()
    print(solution.FindMaxConsecutiveOnes([1,0,1,1,0,1]))
    
if __name__ == '__main__':
    main()
        
        