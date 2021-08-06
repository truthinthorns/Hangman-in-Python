import random
from os import system

def getword():
    words = ["hamburger","pizza","burrito","salad","fried rice","french fries","shake","noodles","hangman"]
    return words[random.randint(0,9)]

def set_guessing_word(word):
    newWord = ""
    for i in range(len(word)):
        if(word[i]==" "):
            newWord += "  "
        else:
            newWord+= "_ "
    return newWord

def update_guessing_word(pos,guessing_word,letter):
    word = list(guessing_word)
    for i in pos:
        word[i + i] = letter
    return word

def get_spaces_to_update_correct_count(word):
    x = 0
    for i in word:
        if(i==" "):
            x+=1
    return x

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
    
def print_wrong_letters(letters):
    print("Wrong letters: ", end=" ")
    for x in letters:
        print(x, end=" ")

def get_positions(letter, word):
    pos = []
    for x in range(len(word)):
        if(word[x]==letter):
            pos.append(x)
    return pos

choice = 0
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