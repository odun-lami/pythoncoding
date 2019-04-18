import random


number = random.randint (0, 100)
#   print (number)

while True:
    guess = input ("Pick a ramdom number from 0-100")
    if guess.isalpha () :
        print ("number, not alphabeth")
        continue
    try:
        guess = int (guess)
    except:
        print ("invalid input")
        continue
    guess = int (guess)
    if guess == number: 
        print ("are you a witch?")
        break
    else:
        print ("you missed it, whore")5
