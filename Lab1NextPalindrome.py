'''
CMSC 142 section 2
Laboratory Exercise 1 

Given an integer n, find the next smallest palindrome integer. 

hello. this is a test repo.
'''

import time

def isPalindrome(numDigits):
    leftIndex = 0
    rightIndex = len(numDigits) - 1

    while leftIndex < rightIndex:
        if numDigits[leftIndex] != numDigits[rightIndex]:
            return False
        
        leftIndex += 1              # Move the left index forward
        rightIndex -= 1             # Move right index backward of the list
    
    return True


def nextPalindrome(n):
    while True:
        n += 1                      # Move to the next integer

        if n == '9' * len(str(n)):              # This accepts integers with digits of 9, 99, etc.
            return n + 2
        
        numDigits = list(str(n))                # Convert integer into a list of strings/digits
        if isPalindrome(numDigits):
            return int("".join(numDigits))      # Convert the list of digits into a single integer


def main():
    startTime = time.time()

    with open("full_input", "r") as file:           # This automatically closes the file after execution
        inputs = file.readlines()                   # Returns all inputs as elements in the list

    numCases = int(inputs[0])                       # The first element of the list = number of test cases                                     
    testCases = [int(inputs[i]) for i in range(1, numCases + 1)]        # Skips the first input since it is the no. of test cases

    for input in testCases:                 # prints the next smallest palindrome integer for each input
        print(nextPalindrome(input))     

    endTime = time.time()
    totalRuntime = endTime - startTime
    print("Total program runtime: " + str(totalRuntime))

main()
