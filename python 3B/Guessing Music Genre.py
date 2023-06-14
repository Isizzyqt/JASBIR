#!/usr/bin/env python

import random

def main():
    """Start a guessing music."""
    print("Guess the music genre!")

    #list the genre
    genre = ["Jazz" ,"Rap","K-POP", "Hiphop", "Disco", "Rock", "Opera", "Electro"]
    x = random.choice(genre)
    guess = None
    
    #check if the input is correct
    while x != guess:
         
        guess = str(input("Pick a genre (Jazz,Rap,K-POP,Hiphop,Disco,Rock,Opera,Electro): "))
        if x == guess:
            print("You're so smart!".format(guess))
            break
        else:
            print("Please try again!".format(guess))
            #give hint to player
            if x == "Jazz":
               print("Swing and blue notes.")
            
            elif x == "Rap":
                print("Mimicry and rhyme.")
            
            elif x == "K-POP":
                print("Sharp dance routines and fashionable.")

            elif x == "Hiphop":
                print("A rhythmic and rhyming speech that is chanted.")

            elif x == "Disco":
                print("Four-on-the-floor beats.")

            elif x == "Rock":
                print("Color, streak, cleavage, luster, and hardness.")

            elif x == "Opera":
                print("A dramatic story told through the use of music and song.")

            elif x == "Electro":
                print("Drum machines and heavy electronic sounds.")

main()        