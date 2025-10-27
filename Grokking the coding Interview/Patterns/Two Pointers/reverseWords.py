'''
    Link: https://www.educative.io/interview-prep/coding/reverse-words-in-a-string

    Problem: Reverse Words in a String
    
    Medium

    Statement
    You are given a string sentence that may contain leading or trailing spaces, as well as multiple spaces 
    between words. Your task is to reverse the order of the words in the sentence without changing the order of 
    characters within each word. Return the resulting modified sentence as a single string with words separated 
    by a single space, and no leading or trailing spaces.

    Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single 
    spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in 
    the returned string, with no leading, trailing, or extra spaces.

    Constraints:

    The sentence contains English uppercase and lowercase letters, digits, and spaces.

    There is at least one word in a sentence.

    1 ≤ sentence.length ≤ 10⁴

    Time Complexity: O(n)

    Space Complexity: O(n)

'''

def reverse_words(sentence):
    
    startCounter = 0

    sentenceLength = len(sentence)

    result = ''

    while startCounter < sentenceLength:
        while ((startCounter < sentenceLength) and  (sentence[startCounter] == ' ')):
            startCounter += 1

        if startCounter >= sentenceLength:
            break

        endCounter = startCounter + 1

        while((endCounter < sentenceLength) and (sentence[endCounter] != ' ')):
            endCounter += 1

        word = sentence[startCounter : endCounter]

        if result == '':
            result = word
        else:
            result = word + ' ' + result

        startCounter = endCounter + 1

    return result

def main():
    print(reverse_words("e"))


if __name__ == '__main__':
    main()