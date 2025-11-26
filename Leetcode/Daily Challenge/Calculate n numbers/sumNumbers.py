"""
    Calculate the sum of n numbers


    Planning
    Use the mathematical formula which is very efficient 

    sum = n (n + 1) / 
    
    Time Complexity: O(1)

    Space Complexity: O(1)

"""

class SumNumbers:
    def calculateSum(self, n):
        sum = n * (n + 1) / 2
        return sum

def main():
    sumNumbers = SumNumbers()

    ans = sumNumbers.calculateSum(2)
    print(f"The sum of the first n numbers is {ans}")


if __name__ == '__main__':
    main()