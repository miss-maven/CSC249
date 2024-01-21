# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:43:17 2024

@author: Maven
"""
# Jane Martin
# CSC-249 
# 01/21/2024

import random 

def main(): 
    print("Lets play rock paper scissors!")
    user_pick = get_user_pick()
    robot_pick = get_robot_pick()
    print(f"The computer chose: {robot_pick}")
    
    print (champ(user_pick, robot_pick))

def get_user_pick():
    user_pick = input("Enter your choice: rock, paper, or scissors: " ).lower()
    user_pick = user_pick.lstrip() # take away white space from entry
    user_pick = user_pick.rstrip() # remove whiote space form end
    
    while user_pick not in ["rock", "paper", "scissors"]: 
        print("Invalid selection please choose from rock, paper, or scissors")
        user_pick = input("Enter your choice of rock, paper, or scissors: ").strip().lower()
        return user_pick
    
def get_robot_pick():
    return random.choice(["rock", "paper", "scissors"])

def champ(user_pick, robot_pick): 
    if user_pick == robot_pick:
        return "It is a tie!!!"
    elif (user_pick == "rock" and robot_pick == "scissors") or \
         (user_pick == "paper" and robot_pick == "rock") or \
         (user_pick == "scissors" and robot_pick == "paper"):
             return "You won!!!"
    else: 
        return "You lost :/ "
    
if __name__ == "__main__":
    main()
    
