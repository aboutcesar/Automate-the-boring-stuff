#! debugging Coin Toss Game

import random, logging

logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s -  %(levelname) s -  %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(f'toss is {toss} ' )
if toss == 0:
    throw = 'tails'
else:
    throw = 'heads'

if throw == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    logging.debug(f'toss is {toss} ')
    logging.debug(f'throw is {throw} ')
    if throw == guess:
        logging.debug(f'toss is {toss} ')
        print('You got it!')
    else:
        logging.debug(f'toss is {toss} ')
        print('Nope. You are really bad at this game.')


