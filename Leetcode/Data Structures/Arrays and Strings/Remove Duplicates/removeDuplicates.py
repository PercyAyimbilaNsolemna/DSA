''''
    A Better Repeated Deletion Algorithm 

    Anyway, the algorithm with O(N) space is surprisingly similar to the one without. Interestingly, it's simpler though, 
    because it doesn't need to firstly determine the size of the output.

    Implementing this requires the use of the two-pointer technique. This is where we iterate over the Array in two 
    different places at the same time.

    Read all the elements like we did before, to identify the duplicates. We call this our readPointer.
    Keep track of the next position in the front to write the next unique element we've found. We call this our writePointer.
'''

class Solution():
    def removeDuplicates(self, nums):
        writeReader = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[writeReader] = nums[i]
                writeReader += 1
            #print(nums)
        #print(writeReader)
        return nums 


def main():
    solution = Solution()
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == '__main__':
    main()