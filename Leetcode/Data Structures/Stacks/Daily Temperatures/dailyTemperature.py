'''

    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
    is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for 
    which this is possible, keep answer[i] == 0 instead.

 

    Example 1:

    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    Example 2:

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    Example 3:

    Input: temperatures = [30,60,90]
    Output: [1,1,0]
    

    Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100

        You are here!
    Your runtime beats 85.69 % of python submissions.

        You are here!
    Your memory usage beats 91.39 % of python submissions.
'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #Creates an array to store the number of days to wait to get a warmer temperature
        ans = [0] * len(temperatures)

        #Stack to keep track of the temperatures
        stack = []

        #Loops through the temperatures
        for index, temp in enumerate(temperatures):
            #Checks if the stack is not and empty and the temp is greater than the temp at the peek of the stack
            while stack and temp > temperatures[stack[-1]]:
                #Removes the index of the top remp from the stack
                popped_index = stack.pop()
                #Calculates the difference between the index of the current temp and the index of the temp popped from the stack
                ans[popped_index] = index - popped_index
 
            #If the stack is empty or the current temp is less than the temp at the top of the stack the index of the pushed to the stack
            stack.append(index)

        return ans


def main():
    solution = Solution()
    print(solution.dailyTemperatures([30,40,50,60]))

    print(solution.dailyTemperatures([30,60,90]))

    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))

if __name__ == '__main__':
    main()