'''
    Link: https://www.educative.io/interview-prep/coding/sort-colors

    Problem: Sort Colors
    Takes 30 mins

    Statement
    Given an array, colors, which contains a combination of the following three elements:

    0 (Representing red)

    1 (Representing white)

    2 (Representing blue)

    Sort the array in place so that the elements of the same color are adjacent, and the final order is: 
    red (0), then white (1), and then blue (2).

    Note: You are not allowed to use any built-in sorting functions. The goal is to solve this efficiently without 
    extra space.

    Constraints:

    n == colors.length

    1 ≤ n ≤ 300

    colors[i] is either 0, 1, or 2

    Time Complexity: O(n)

    Space Complexity: O(n)

'''

def sort_colors(colors):
    #Declares left and right pointers
    left, middle, right = 0, 0, len(colors) - 1

    while middle <= right:
        if colors[left] == 0:
            left += 1
            middle += 1

        elif colors[right] == 2:
            right -= 1

        elif colors[left] == 2:
            colors[right], colors[left] = colors[left], colors[right]
            right -= 1

        elif colors[middle] == 1:
            middle += 1

        elif colors[middle] == 0:
            colors[left], colors[middle] = colors[middle], colors[left]
            left += 1
            middle += 1

        elif colors[middle] == 2:
            colors[middle], colors[right] = colors[right], colors[middle]
            right -= 1

    return colors

def main():
    print(sort_colors([2, 2, 1, 1, 0, 0]))

if __name__ == '__main__':
    main()