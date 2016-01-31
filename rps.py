#!/usr/bin/env python3.5
from random import randint
import sys
import os


def init_scores():

	comp_score = 0
	user_score = 0
	user_pick(comp_score, user_score)

def user_pick(comp_score, user_score):

	draw = input("Do you pick [R]ock, [P]aper, or [S]cissors? "
					  "Type the first letter. ").lower()

	if draw in 'rps':

		if draw == 'r':

			draw = 'rock'

		if draw == 'p':

			draw = 'paper'

		if draw == 's':

			draw = 'scissors'

	else:

		print("That was not a letter of any of the options. Try again.")
		user_pick(comp_score, user_score)

	ai_pick(draw, comp_score, user_score)

def ai_pick(user_choice, comp_score, user_score):

	clear()
	options = ['rock', 'paper', 'scissors']
	comp_gen = randint(0, 2)
	comp_choice = options[comp_gen]
	
	comp_win_options(comp_choice, user_choice, comp_score, user_score)

	user_win_options(comp_choice, user_choice, comp_score, user_score)

	tie_options(comp_choice, user_choice, comp_score, user_score)

def comp_win(ai_choice, user_choice, computer_score, player_score):

	print("The computer picked {} and you picked {}."
		  "The computer wins the round! \n".format(ai_choice, user_choice))
	print("The current score is \n"
		  "Computer: {} \n"
		  "Player: {} \n".format(computer_score, player_score))
	play_again(computer_score, player_score)

def user_win(ai_choice, user_choice, computer_score, player_score):

	print("The computer picked {} and you picked {}."
		  "You win the round! \n".format(ai_choice, user_choice))
	print("The current score is \n"
		  "Computer: {} \n"
		  "Player: {} \n".format(computer_score, player_score))
	play_again(computer_score, player_score)

def add_ai_score(computer_score):

	computer_score += 1

	return computer_score

def add_user_score(player_score):

	player_score += 1

	return player_score

def tie(comp_score, user_score):

	print("You tied! Redo the round.")
	user_pick(comp_score, user_score)

def clear():

	if os.name == 'nt':

		os.system('cls')

	else:

		os.system('clear')

def play_again(comp_score, user_score):

	another_round = input("Play another round? Y/n ").lower()

	if another_round != 'n':

		user_pick(comp_score, user_score)

	else:

		if comp_score > user_score:

			print("The computer is the winner!")
			exit()

		elif user_score > comp_score:

			print("You are the winnter!")
			exit()

		else:

			print("You both had the same score!")
			exit()

def comp_win_options(comp_choice, user_choice, comp_score, user_score):

	if comp_choice == 'rock' and user_choice == 'scissors':

		comp_win(comp_choice, user_choice, add_ai_score(comp_score), user_score)

	elif comp_choice == 'paper' and user_choice == 'rock':

		comp_win(comp_choice, user_choice, add_ai_score(comp_score), user_score)

	elif comp_choice == 'scissors' and user_choice == 'paper':

		comp_win(comp_choice, user_choice, add_ai_score(comp_score), user_score)

def user_win_options(comp_choice, user_choice, comp_score, user_score):
	
	if comp_choice == 'rock' and user_choice == 'paper':

			user_win(comp_choice, user_choice, comp_score, add_user_score(user_score))

	elif comp_choice == 'paper' and user_choice == 'scissors':

		user_win(comp_choice, user_choice, comp_score, add_user_score(user_score))

	elif comp_choice == 'scissors' and user_choice == 'rock':

			user_win(comp_choice, user_choice, comp_score, add_user_score(user_score))

def tie_options(comp_choice, user_choice, comp_score, user_score):

	if comp_choice == 'rock' and user_choice == 'rock':

			tie(comp_score, user_score)

	elif comp_choice == 'paper' and user_choice == 'paper':

		tie(comp_score, user_score)

	elif comp_choice == 'scissors' and user_choice == 'scissors':

		tie(comp_score, user_score)

def exit():

	print("Thanks for playing!")
	sys.exit()

init_scores()