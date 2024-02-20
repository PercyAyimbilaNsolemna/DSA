'''
    Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does
    not exist, return the maximum number.

    Example 1:

    Input: nums = [3,2,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2.
    The third distinct maximum is 1.
    Example 2:

    Input: nums = [1,2]
    Output: 2
    Explanation:
    The first distinct maximum is 2.
    The second distinct maximum is 1.
    The third distinct maximum does not exist, so the maximum (2) is returned instead.
    Example 3:

    Input: nums = [2,2,3,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.
    

    Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1
    

    Follow up: Can you find an O(n) solution?

'''

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        setNums = list(set(nums))

        if len(setNums) <= 2:
            return max(setNums)
        
        negativeNums = []
        
        for num in setNums:
            if num < 0:
                print(num)
                negativeNums.append(num)
                setNums.remove(num)

        setNums = negativeNums + setNums

        print(negativeNums)

        print(setNums)

        return setNums[len(setNums)-3]


def main():
    solution = Solution()

    print(solution.thirdMax([-1,2,3,-2]))


if __name__ == '__main__':
    main()