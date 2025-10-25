'''
    Link: 


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