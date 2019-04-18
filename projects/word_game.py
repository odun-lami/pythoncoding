import random

words = ['dany',  'jon', 'cersei', 'arya']

answer = random.choice(words).lower() 

#print (answer)

def scramble(i):
    i = list(i)
    random.shuffle(i)
    #print(i)
    scrambled_word = ''.join(i)

    return scrambled_word

shuffled = scramble(answer)

print(shuffled)

guess = input ("Guess the GoT Character:")
guess = guess.lower ()

while True:
    if guess == answer:
        print ("You Sabi")
        break
    else:
        print ("Nope")

