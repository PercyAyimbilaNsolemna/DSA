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

    TO BE OPTIMIZED

'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #Creates an array to store the number of days to wait to get a warmer temperature
        ans = []

        #Stack to keep track of the temperatures
        stack = []

        for temp in temperatures:
            #Appends the temp to tyhe stack if the stack is empty
            if not stack:
                stack.append(temp)
            else:
                if temp > stack[-1]:
                    ans.append(len(stack))
                    stack.clear()
                    stack.append(temp)
                else:
                    stack.append(temp)
                    stack[-1], stack[-2] = stack[-2], stack[-1]

            print(stack)

        return ans


def main():
    solution = Solution()
    print(solution.dailyTemperatures([30,40,50,60]))



if __name__ == '__main__':
    main()