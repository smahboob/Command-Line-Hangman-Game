import random
import sys
from collections import Counter 
import time
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer


def pickWord(level):

	fin = open('easy.txt' , 'r')
	easyList = []
	contentss = fin.readlines()
	for i in range(len(contentss)):
		easyList.append(contentss[i].strip('\n'))


	fin2 = open('medium.txt' , 'r')
	mediumList = []
	contentss = fin2.readlines()
	for i in range(len(contentss)):
		mediumList.append(contentss[i].strip('\n'))


	fin3= open('hard.txt' , 'r')
	hardList = []
	contentss = fin3.readlines()
	for i in range(len(contentss)):
		hardList.append(contentss[i].strip('\n'))

    
	if level in 'eE':
		word = random.choice(easyList)
	elif level in 'mM':
		word = random.choice(mediumList)
	elif level in 'hH':
		word = random.choice(hardList)
	else:
		print("Choose from 'e', 'm' , 'h' only")
		level = str(input('Which level do you want to play, Easy(e), Medium(m) or Hard(h):'))
		if level in 'eE':
			word = random.choice(easyList)
		elif level in 'mM':
			word = random.choice(mediumList)
		elif level in 'hH':
			word = random.choice(hardList)

	return word


def song(mixer):

	mixer.init() 
	mixer.music.load("gaming.mp3")
	mixer.music.play()

	music = input("Press 'm' to mute or 'p' to play the music:")
	if music == 'm':
		 mixer.music.stop()

	elif music == 'p':
		 mixer.music.play()

def need_help(help):

	help = input("Enter 'h' to get help or 'p' to continue playing:")
	Help22 = "Hangman is a quick and easy game for at least two people that requires nothing more than paper, a pencil, and the ability to spell. One player, the host makes up a secret word, while the other player tries to guess the word by asking what letters it contains. However, every wrong guess brings them one step closer to losing."
	if help in 'h':
		print(Help22)
	else:
		game = True 

	return help


def checkword(guessWord, alreadyGuessedLetters, chances, word):
	chances = 8

	if guessWord.isalpha() == False:
		chances = chances + 1
		print('You can only enter a letter') 
	     
	elif len(guessWord) > 1:
		print('Enter only a single letter at a time') 
		guessWord = str(input('Enter a letter to Guess:'))

	elif guessWord in alreadyGuessedLetters:
		print('You have already tried this letter, Try something new') 
			
	return guessWord, alreadyGuessedLetters, chances, word


def hang_the_man(chances, chancesGiven, stages):

	e = chancesGiven - chances 
				
	print("\n", '\n'
          .join(stages[0:e]))
	print('\n' , 'Chances left:' ,chances)

	return e, chancesGiven , chances , stages



def main():
	stages = [
                '\t  _______ ',
                '\t  |     | ',
                '\t  |     | ',
                '\t  O     | ',
                '\t \|/    | ',
                '\t  |     | ',
                '\t / \\    | ',
                '\t        | ',
                '\t________|_',
            ]

	game = True
	name = input('Please enter your name:')
	print(name[0].upper() + name[1:], 'Welcome to the Hangman Game')

	#PLAY THE MUSIC
	song(mixer)
	need_help(help)

	level = str(input('Which level do you want to play, Easy(e), Medium(m) or Hard(h):'))
	word = pickWord(level)

	if __name__ == '__main__':
		for i in word: 
			print('_', end = '  ')		 
		print() 
	
		game = True
		chancesGiven = 8
		chances = 8
		correctMove = 0
		alreadyGuessedLetters = ''
		winStreak = 0
		Lost = 0
		Win = 0
		allwords = ''
		wrongguess = ''

		try:
			while chances != 0 and game:
				print()

				try:
					guessWord = str(input('Enter a letter to Guess:'))
				except:
					print ('You can only enter a letter') 
					checkword(guessWord, alreadyGuessedLetters, chances, word)
					continue

				if guessWord in word:
					alreadyGuessedLetters = alreadyGuessedLetters + (guessWord * dict(Counter(word).items())[guessWord])

				for character in word:
					if character in alreadyGuessedLetters:
						print(character, end = '  ')
						correctMove = correctMove + 1
					else:
						print('_' , end ='  ')

				if guessWord not in word:
					chances = chances - 1
					for i in guessWord:
						wrongguess = wrongguess + i + '  ' 
						print('\n',wrongguess , end = '  ')

				
				
				hang_the_man(chances, chancesGiven, stages)
				
		

				if Counter(alreadyGuessedLetters) == Counter(word):  
					print()
					print ('CONGRAGULATIONS', name.upper(), 'YOU HAVE WON THE GAME')
					winStreak = winStreak + 1
					game = False

				if chances == 0:
					print()
					print('Sorry', name[0].upper() + name[1:],  'you lost, Please try again')
					print ('The actual word was:' , word)
					Lost = Lost + 1
					game = False	


				if game == False:
					print('Won = ',winStreak)
					print('Lost = ',Lost)

					play = input('Do yo want to play again y/n? ')
					if play in 'yY':
						game = True
						level = str(input('Which level do you want to play, Easy(e), Medium(m) or Hard(h):'))
						word = pickWord(level)
						chancesGiven = 8
						chances = 8
						correctMove = 0
						wrongguess = ''
						alreadyGuessedLetters = ''
						for i in word: 
							print('_', end = '  ')

					else:
						mixer.music.stop()
						sys.exit(0)

	

		except KeyboardInterrupt:
			print()
			print('Bye Try again')
			sys.exit(0)
main()
