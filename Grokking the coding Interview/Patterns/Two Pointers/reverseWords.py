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
    
    #Declares and initializes the startCounter which starts a word count
    startCounter = 0

    #Gets the length of the sentence
    sentenceLength = len(sentence)

    #Initialize an empty string to hold the reversed sentence
    result = ''

    #Loops through the sentence if the startCounter is less than the length of the sentence
    while startCounter < sentenceLength:
        
        #Ignores all whitespaces before a word
        while ((startCounter < sentenceLength) and  (sentence[startCounter] == ' ')):
            startCounter += 1

        #Breaks out of the while loop if the startCounter hits the end of the sentence
        if startCounter >= sentenceLength:
            break
        
        #Initialize the word endCounter to one ahead of the startCounter after the startCounter hits the start of a word
        endCounter = startCounter + 1

        #Ends the counting of a word when a space is seen
        while((endCounter < sentenceLength) and (sentence[endCounter] != ' ')):
            endCounter += 1

        #Extracts the word from the sentence using python list comprehension
        word = sentence[startCounter : endCounter]

        #Checks if the reult is an empty string then set the word to the result, if not add the word to the begining 
        #of the result and add a space 
        if result == '':
            result = word
        else:
            result = word + ' ' + result

        #Set the startCounter to the endCounter and add one since we want to start from the next character after the
        #previous word
        startCounter = endCounter + 1
        
    #Return the result
    return result

def main():
    print(reverse_words("e"))


if __name__ == '__main__':
    main()