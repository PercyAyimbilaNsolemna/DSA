'''
    Duplicate zeros
    
    Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

    Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

    Example 1
        Input: arr = [1,0,2,3,0,4,5,0]
        Output: [1,0,0,2,3,0,0,4]
        Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
        
    Example 2
        Input: arr = [1,2,3]
        Output: [1,2,3]
        Explanation: After calling your function, the input array is modified to: [1,2,3]
        
    Constraints
        1 <= arr.length <= 104
        0 <= arr[i] <= 9
        
    Algorithm
    Insert a zero after a zero is encountered 
    Check if the length of the new array is equal to the original length of the array
    If it is return the list if not continue
     
'''

class Solution(object):
    def duplicateZeros(self, arr):
        array_size = len(arr)
        new_array = []
        
        #Loops through the initial array and duplicate any zero found
        for index in range(len(arr)):
            #Ends the for loop if the new_array size is equal or greater than the original array
            if len(new_array) >= array_size:
                #Trims the new array to have the same size as the original array
                new_array = new_array[:array_size]
                break
            elif arr[index] == 0:
                new_array.append(0)
                new_array.append(0)
            else:
                new_array.append(arr[index])
        
        #Inserts each element in the new array to the original array
        for index in range(len(new_array)):
            arr[index] = new_array[index]
        
        return arr      
        
    
def main():
    solution = Solution()
    print(solution.duplicateZeros([0,0,0,0,0,0,0]))
    
    
if __name__ == '__main__':
    main()