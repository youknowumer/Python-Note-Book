# -*- coding: utf-8 -*-
"""practice paper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17foibfpINTUGNnKIjmzNJ1lNKNAgpYk4
"""

import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")

import datetime
y = int(input("Enter year of birth: "))
m = int(input("Enter month of birth: "))
d = int(input("Enter day of birth: "))
b = datetime.datetime(y, m, d)
print(b.strftime("%d-%m-%Y"))
def astro_sign(d, m):
 if m == 1 and d >= 20 or m == 2 and d <= 18:
    return "Aquarius"
 elif m == 2 and d >= 19 or m == 3 and d <= 20:
     return "Pisces"
 elif m == 3 and d >= 21 or m == 4 and d <= 19:
     return "Aries"
 elif m == 4 and d >= 20 or m == 5 and d <= 20:
     return "Taurus"
 elif m == 5 and d >= 21 or m == 6 and d <= 20:
     return "Gemini"
 elif m == 6 and d >= 21 or m == 7 and d <= 22:
     return "Cancer"
 elif m == 7 and d >= 23 or m == 8 and d <= 22:
     return "Leo"
 elif m == 8 and d >= 23 or m == 9 and d <= 22:
     return "Virgo"
 elif m == 9 and d >= 23 or m == 10 and d <= 22:
     return "Libra"
 elif m == 10 and d >= 23 or m == 11 and d <= 21:
     return "Scorpio"
 elif m == 11 and d >= 22 or m == 12 and d <= 21:
     return "Sagittarius"
 elif m == 12 and d >= 22 or m == 1 and d <= 19:
     return "Capricorn"
 else:
        return "Invalid date"
sign = astro_sign(d, m)
print("Your astrological sign is:", sign)

import random
def guess_number():
    number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("You guessed the number!")
    else:
        print("You guessed wrong. The number was", number)
if __name__ == "main":
    guess_number()

import random

def guess_number():
  number = random.randint(1, 1000)
  guess = None
  attempts = 0
  while guess != number:
   guess = int(input("Guess a number between 1 and 1000: "))
   attempts += 1
    if guess < number:
      print("Your guess is too low.")
    elif guess > number:
      print("Your guess is too high.")
    else:
      print(f "Congratulations! You guessed the number in {attempts} attempts.")
   def play_again():
  answer = input("Would you like to play again? (y/n): ")
  return answer == "y"

if __name__ == "__main__":
  while True:
    guess_number()
    if not play_again():
      break

import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
      print("you guessed the no")