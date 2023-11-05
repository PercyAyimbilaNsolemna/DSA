'''
    Merge Sorted Array
    
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
    representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    
    Example1
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    
    Example 2
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    
    Example 3
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can 
    fit in nums1

    Constraints
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
 

    Follow up: Can you come up with an algorithm that runs in O(m + n) time?

    Algorithm
    variables to keep track of the len of num1 and num2 already given
    Use two pointers to iterate over both arrays
    Check the values at each index, append the greater one to the new array and move that pointer one up
    If the index in the second array gets to the last index, append all the numbers left in num1 array 
    Excluding the zeros
    Insert the sorted array into a new array
    After that transfer the elements in the sorted array to num1 array
'''

class Solution(object):
     def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num1Counter = 0
        num2Counter = 0
        sortedArray = []
        
        while num1Counter <= m and num2Counter <= n:
            print(nums1)
            #print(num2Counter)
            if num2Counter == n - 1 or num1Counter == m - 1:
                #Modify this block of code to accomplish the required task
                if num2Counter == n-1:
                    if nums2[num2Counter] < nums1[num1Counter]:
                        sortedArray.append(nums2[num2Counter])
                        sortedArray.append(nums1[num1Counter: ])
                    else:
                        sortedArray.append(nums1[num1Counter])
                        sortedArray.append(nums2[num2Counter: ])
                else: 
                    if nums2[num2Counter] < nums1[num1Counter]:
                        sortedArray.append(nums2[num2Counter])
                        sortedArray.append(nums1[num1Counter: ])
                    else:
                        sortedArray.append(nums1[num1Counter])
                        sortedArray.append(nums2[num2Counter: ])                   
                print(num2Counter)
                break
            elif nums2[num2Counter] < nums1[num1Counter]:
                sortedArray.append(nums2[num2Counter])
                num2Counter += 1
            else:
                sortedArray.append(nums1[num1Counter])
                num1Counter += 1
        print(sortedArray)
            
    
def main():
    solution = Solution()
    print(solution.merge([1,2,3,0,0,0], 6, [2,5,6], 3))
    
if __name__ == '__main__':
    main()