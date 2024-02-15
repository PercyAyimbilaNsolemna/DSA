'''
    Given an integer array nums, move all 0's to the end of it while maintaining the relative 
    order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Example 2:

    Input: nums = [0]
    Output: [0]
    

    Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    

    Follow up: Could you minimize the total number of operations done?

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        writeReader = len(nums)

        for index in range(len(nums)):
            if nums[index] == 0:
                for j in range(index, writeReader-1):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    
                writeReader -= 1
          
        return nums
    
    def optimizedMoveZeros(self, nums):
        writeReader = len(nums)

        for index in reversed(range(len(nums))):
            if nums[index] == 0:
                for j in range(index, writeReader-1):
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                
                writeReader -= 1

        return nums

def main():
    solution = Solution()

    #print(solution.moveZeroes([0,1,0,3,12]))

    print(solution.optimizedMoveZeros([0,1,0,3,12]))


if __name__ == '__main__':
    main()