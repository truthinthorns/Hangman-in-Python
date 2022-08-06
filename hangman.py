import random
from os import system
import sys

#opens the file and reads each of the lines in it, removing any whitespace, then choosing a random index in the listOfWords list.
#if the length of the chosen word is less than 3, choose a new word.
#if the length of word is at least 3, return that word.
def getword():
    #need to change the location of the words list used here.
    wordFile = open("C:/Users/Desktop/wordList.txt","r")
    tempwords = wordFile.readlines()
    listofwords = []
    for i in range(len(tempwords)):
        listofwords.append(tempwords[i].strip())
    word = listofwords[random.randint(0,len(listofwords)-1)]
    while(len(word) < 3):
        word = listofwords[random.randint(0,len(listofwords)-1)]
    return word

#if there is a space in the word, add two spaces to the output for formatting. makes it more clear that there are separate words.
def set_guessing_word(word):
    newWord = ""
    for i in range(len(word)):
        if(word[i]==" "):
            newWord += "  "
        else:
            newWord+= "_ "
    return newWord

#set the guessed letter at each occurence.
def update_guessing_word(pos,guessing_word,letter):
    word = list(guessing_word)
    for i in pos:
        #this is necessary because of the spaces in guessing_word.
        word[i+i] = letter
    return word

#to win, it's based on the value of correct_count. since spaces can't and shouldn't be guessed, for each space, increment x. return it at the end to add it to correct_count.
def get_spaces_to_update_correct_count(word):
    x = 0
    for i in word:
        if(i==" "):
            x+=1
    return x

#this one should be pretty easy to figure out. just prints out the hangman character based on how many guesses the player has left.
def print_hangman(errors_remaining):
    if(errors_remaining==6):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|_____________________")
    elif(errors_remaining==5):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /   \\")
        print("|	       \ _ /")
        print("|\n|\n|\n|\n|\n|\n|\n|\n|\n|_____________________")
    elif(errors_remaining==4):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /   \\")
        print("|	       \ _ /")
        print("|		 |")
        print("|		 |")
        print("|		 |")
        print("|		 |")
        print("|		 |")
        print("|\n|\n|\n|_____________________")
    elif(errors_remaining==3):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /   \\")
        print("|	       \ _ /")
        print("|		 |")
        print("|	       \ | ")
        print("|		\| ")
        print("|		 |")
        print("|		 |")
        print("|\n|\n|\n|_____________________")
    elif(errors_remaining==2):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /   \\")
        print("|	       \ _ /")
        print("|		 |")
        print("|	       \ | /")
        print("|		\|/ ")
        print("|		 |")
        print("|		 |")
        print("|\n|\n|\n|_____________________")
    elif(errors_remaining==1):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /   \\")
        print("|	       \ _ /")
        print("|		 |")
        print("|	       \ | /")
        print("|		\|/ ")
        print("|		 |")
        print("|		 |")
        print("|		/")
        print("|	       /")
        print("|\n|_____________________")
    elif(errors_remaining==0):
        print(" ________________")
        print("|		 |")
        print("|		 |")
        print("|	         |")
        print("|	  	 _")
        print("|	       /x x\\")
        print("|	       \ _ /")
        print("|		 |")
        print("|	       \ | /")
        print("|		\|/ ")
        print("|		 |")
        print("|		 |")
        print("|		/ \\")
        print("|	       /   \\")
        print("|\n|_____________________")
    
#print out the incorrectly guessed letters.    
def print_wrong_letters(letters):
    print("Wrong letters: ", end=" ")
    for x in letters:
        print(x, end=" ")

#if the letter is in the word, return the position(s) that the letter occurs in the word.
def get_positions(letter, word):
    pos = []
    for x in range(len(word)):
        if(word[x]==letter):
            pos.append(x)
    return pos

choice = 0

#this is just the main loop. there isn't anything crazy going on here, so I don't see a reason to comment it much.
#it essentially initializes everything for the game, and runs a loop while the user hasn't won/lost. it updates the UI to reflect how the user is doing, and shows messages based on if the user ends up winning or losing.
while(choice!=2):
    print("\nEnter a choice:\n1)Play\n2)Quit")
    choice = int(input())
    if(choice!=2):
        random.seed()   
        word = getword()
        wrong_letters = []
        correct_count = 0
        errors_remaining = 6
        guessing_word = set_guessing_word(word)
        correct_count += get_spaces_to_update_correct_count(word)
        while(True):
            system('cls')
            print_hangman(errors_remaining)
            print("\n" + guessing_word)
            print_wrong_letters(wrong_letters)
            print("\nChances left:", end=" ")
            print(errors_remaining)
            print("Enter a letter:", end=" ")
            letter = input()
            while(letter in wrong_letters or letter in guessing_word):
                print("You already tried that letter! Try again!")
                letter = input()
            if(letter in word):
                x = get_positions(letter, word)
                guessing_word = ''.join(update_guessing_word(x, guessing_word, letter))
                print(guessing_word)
                correct_count += len(x)
                if(correct_count == len(word)):
                    system('cls')
                    print("YOU WIN!")
                    print_hangman(errors_remaining)
                    print("\n" + guessing_word)
                    print_wrong_letters(wrong_letters)
                    print("\nChances left: ", end=" ")
                    print(errors_remaining)
                    break
            else:
                wrong_letters.append(letter)
                errors_remaining-=1
                if(errors_remaining==0):
                    system('cls')
                    print_hangman(errors_remaining)
                    print("You lose!\nThe word was:", end = " ")
                    print(word)
                    break
