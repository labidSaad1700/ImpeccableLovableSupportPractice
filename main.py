# ImpeccableLovableSupportPractice
Python simple code for practise

'use strict'

# Weight converter

weightAsking = input('I want to convert my weight in : ')

def weightAskingFunction():
  if weightAsking == ('Kg' or 'kg' or 'KG'):
    weightAskingForPound = int(input('Enter your kg weight: '))
    print(weightAskingForPound * 2.2)
  elif weightAsking == ('pound' or 'Pound' or 'POUND'):
    weightAskingForKG = int(input('Enter your pound weight: '))
    print(weightAskingForKG / 2.2)
  else:
    print('Invalid Input')

weightAskingFunction()

# Guessing Game

number = 9
guessCount = 0
guessCountLimit = 3

while guessCount < guessCountLimit:
  guess = int(input('Enter A Number: '))
  guessCount += 1
  if guess == number:
    print('You won!!')
  if (guessCount == guessCountLimit):
    print('You loose..')

# Building a car game

userInput = input('Enter a command: ')

if(userInput == 'help' or userInput == 'Help'):
  print("start = To start a car")
  print("stop = To stop a car")
  print("end = To end the game")

# Shopping list

list = [10, 20, 30]
total = 0

for i in list:
  total += i
  
print(f'Total: {total}')

list = [20, 50, 80]
sum = 0

for i in list:
  sum += i

print(f'Total: {sum}')


list = [30, 70, 110]
add = 0;

for i in list:
  add += i

x = [150,200,190]
sum = 0

for i in x:
  sum += i

print(f'Total: {sum}')


x = range(20)
sum = 0

for i in x:
  sum += i+1

print(f'Summation of 1-20 is: {sum}')




def function():
  
  enterPreunerMoney = int(input('Enter How much You want to Invest: '))
  mushroomPerpiece = int(input('Enter Per Piece Mushroom Seed Price: '))
  
  mushroomYouCanBuy = float(enterPreunerMoney / mushroomPerpiece)
  mushroomProductionPerWeek = int(input('Enter Mushroom You Have Grown Per Week: '))
  mushroomProductionPerMonth = int(input('Enter How many times You Sell Mushroom Per Month: '))
  
  mushroomYouGetInMonth = mushroomYouCanBuy * mushroomProductionPerWeek *     mushroomProductionPerMonth
  
  mushroomInKGQuantity = mushroomYouGetInMonth / 1000
  
  mushroomPrice = int(input('Enter Mushroom Price Now: '))
  
  mushroomPriceNow = mushroomInKGQuantity * mushroomPrice

  return mushroomPriceNow


print(function())



# Measure Your BMR (How much calory should you nead everyday)

weight = int(input('Enter Your Weight in KG: '))
height = float(input('Enter Your Height in cm: '))
# age = int(input('Enter Your Age in years: '))


# bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age);
# print(bmr)

# # Measure BMI

bmi = weight / (height / 100) ** 2
print(bmi)

if bmi < 18.5:
  print('Your BMI is low')
elif bmi < 25 and bmi > 18.5:
  print('Your BMI is Ideal')
elif bmi < 30 and bmi > 25:
  print('Your BMI is Overweight')
elif bmi < 35 and bmi > 30:
  print('Your Bmi is Obese')
else:
  print('Your BMI is Clinically Obese')


xmMarks = 71;


def passMark():
  if xmMarks >= 40 and xmMarks < 80:
    print('You have passed');
  elif xmMarks < 40:
    print('You have failed');
  elif xmMarks > 80 and xmMarks < 90:
    print('You Got A+')
  elif xmMarks >= 90 and xmMarks < 95:
    print('You have Earned Golden Badge');
  elif xmMarks >= 95:
    print('You have Earned Platinum Badge')
  else:
    print('Result Not Found')


passMark();


