def print_letters(my_word):
        #overview:
    '''Takes a word made up of the letters F, R, I, E, N, D and prints each letter
    as a 5x5 asterisk pattern. Each character is displayed side-by-side in one line.
    Only uppercase letters from 'FRIEND' are supported.'''

#Loops through each row and column of the 5x5 grid for every letter in the word.
    for i in range(0,5):
        for letter in my_word:
            for j in range(0,5):

                if letter == "F":     # Print F in asterisk pattern
                    if ((j == 0 or i == 0) or i == 2):
                        """'F' letter has a full top row, a vertical line down the left
                        and a middle"""
                        print('*', end='')
                    else:
                        print(' ', end='') #This allows for continuous output on the same line (in all letters)

                elif letter == "R":   # Print R in asterisk pattern
                    '''Print R in asterisk using these conditionss'''
                    if (j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or
                       (i == 1 and j == 4) or (i == 3 and j == 2) or
                       (i == 4 and j == 3)):
                        print('*', end='')
                    else:
                        print(' ', end='')

                elif letter == "I":   # Print I in asterisk pattern
                    if ((i == 0 or i == 4) or j == 2):
                        '''forms the letter I with a horizontal line at the top and bottom,
                           plus a central vertical line from top to bottom'''
                        print('*', end='')
                    else:
                        print(' ', end='')

                elif letter == "E":   # Print E in asterisk pattern
                    if ((j == 0 or i == 0) or (i == 2 or i == 4)):
                        '''Forms the letter E using a vertical bar on the left 
                        and three horizontal bars at the top, middle, and bottom'''
                        print('*', end='')
                    else:
                        print(' ', end='')

                elif letter == "N":  # Print N in asterisk pattern
                    if ((j == 0 or j == 4) or i == j):
                        '''Renders the letter N with vertical lines on both ends
                           and a diagonal line from top-left to bottom-right'''
                        print('*', end='')
                    else:
                        print(' ', end='')

                elif letter == 'D':  # Print D in asterisk pattern
                    if (j == 0 or (i == 0 and j < 4) or
                       (i == 4 and j < 4) or
                       (j == 4 and i != 0 and i != 4)):
                        '''Forms the letter D using these if conditons'''
                        print('*', end='')
                    else:
                        print(' ', end='')
                else:   # If the letter is not valid, print an Invalid message
                    print("Invalid input! Please use only uppercase letters.")
                    return

            print(' ', end='') # Print a Space between letters
        print()

#Main Function
def main():
    '''This function handles the main loop of the program. It keeps asking the user to enter words made up 
    of the letters F, R, I, E, N, D and checks if the input is valid. If everything looks good, it prints 
    the word in ASCII art. The loop continues until the user types 'EXIT', at which point it prints a 
    thank-you message and ends the session. Invalid entries are caught with a friendly reminder.'''

    while True:  #While loop to Keep the code ongoing until "EXIT" has been input

        word = input("\nEnter words with letters F, R, I, E, N, D or Type exit to end: ")

        if word.lower() == "exit":         #If Statement defining "EXIT".
            print("Thankyou for Playing") #Print a message Thankyou for Playing.
            break

        correct_words = "FRIEND"
        correct = True # Assume input is right in the beginning

        # Iterates each letters from the input and make sure input is within the guidelines.
        for letter in word:
            if letter not in correct_words:   #Check the letter does not fall under the excluded (invalid) letters category.
                correct = False
                break   #If input is not within the guidelines, redefine rule and ask again.

        if correct:   #If all letters are correct print the words.
            print_letters(word)
        else: #If the input is not correct Print Invalid input message.
            print("Invalid input! Use only uppercase letters from these words F, R, I, E, N, D or Type exit to end.")


            
main() #run the whole program