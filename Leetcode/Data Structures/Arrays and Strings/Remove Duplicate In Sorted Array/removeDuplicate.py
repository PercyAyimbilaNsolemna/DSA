'''
    Remove Duplicates from Sorted Array
    
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they 
    were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    
    Example 1
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Example 2
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 
    respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    
    Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
    
    Algorithm 
    Declare a count to kept track of the non-repetitive numbers we are inserting into the array
    Declare a variable to store the first element in the array
    If the next item is the same then do not insert it into the array and leave the variable as same
    Only change the variable if the new number is not the same as the previous number
'''

class Solution(object):
    def removeDuplicate(self, nums):
        #Counts all unrepeated elements, starts from 1 because the first element is automatically added
        counter = 1
        
        #Loops through the array
        for index in range(1, len(nums)):
            #Checks if the prevoius number is not the same as the current bumber
            if nums[index] != nums[index-1]:
                nums[counter] = nums[index]
                counter += 1
        #print(nums)
        #Returns counter which is the number of unrepeated numbers in the array
        return counter
                
                
        
def main():
    solution = Solution()
    print(solution.removeDuplicate([0,0,1,1,1,2,2,3,3,4]))
    #[1,1,2]
    #[0,0,1,1,1,2,2,3,3,4]
    
if __name__ == '__main__':
    main()