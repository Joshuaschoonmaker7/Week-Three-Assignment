# PigLatin.py
# Author: Joshua Schoonmaker
# CIS 125 IWU

# 1. The program should prompt the user to enter an English word to translate.
# 2. The program should translate the word in to Simple Pig Latin, given the following rules.
# 3. The program should print the translated word.

def main():
    
    # Initial input statements
    print("This program translates any word into its Pig Latin equivalent")
    
    print()
    eWord = input("Please enter an English word: ")
    
    # Variable
    
    vowels = "aeiou"
    
    # if/else statement
    
    if eWord[0] in vowels :
        print()
        print("This word starts with a vowel, so it is translated to: ")
        print()
        print(eWord + "yay")
    else:
        print()
        print("This word starts with a consonant, so it is translated to: ")
        b = eWord[0]
        a = eWord[1:]
        print()
        print(a + b + "ay")
        
main()