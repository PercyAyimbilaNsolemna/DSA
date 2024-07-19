'''
    1365. How Many Numbers Are Smaller Than the Current Number
    Easy


    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
    That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

    Return the answer in an array.

    

    Example 1:

    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Explanation: 
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1). 
    For nums[3]=2 there exist one smaller number than it (1). 
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
    Example 2:

    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
    Example 3:

    Input: nums = [7,7,7,7]
    Output: [0,0,0,0]
    

    Constraints:

    2 <= nums.length <= 500
    0 <= nums[i] <= 100

    
    O(N²) Brute Force solution
    
'''

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Sets a countLess variable to count the number of elements less than the current element
        countLess = 0

        #Initialize an array to store all the numbers less than the current element
        smallerNumbers = []

        #Loop to iterate through all the numbers in nums
        for i in range(len(nums)):
            #Loops through the nums again to find all numbers less than the current element
            for j in range(len(nums)):
                #Checks if the number at i is greater than the number at j
                if nums[i] > nums[j]:
                    #Increment the countLess by one
                    countLess += 1
            #Appends the countLess to the smallesrNumbers array
            smallerNumbers.append(countLess)
            #Resets the countLess variable to zero after each iteration
            countLess = 0

        #Returns the smallerNumbers array
        return smallerNumbers


def main():
    solution = Solution()

    print(solution.smallerNumbersThanCurrent([7,7,7,7]))


if __name__ == '__main__':
    main()