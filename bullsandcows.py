import random
import sys
from time import time

def cow_bull(hadane_cislo, hladane_cislo):
    '''Vygeneruje informaciu o uspesnosti tipu v spravnom tvare.'''
    bull = 0
    for i in range(4):
        if hadane_cislo[i] == hladane_cislo[i]:
            bull += 1
    cow = len(set(hadane_cislo).intersection(set(hladane_cislo))) - bull
    cow_str = 'cow' if cow == 1 else 'cows'
    bull_str = 'bull' if bull == 1 else 'bulls'

    return ('{} {}'.format(bull, bull_str),'{} {}'.format(cow, cow_str))

def vyhodnot(pocet_pokusov):
    '''Podla poctu pokusov vytvori odpoved.'''
    odpoved = 'You must be a genius!' if pocet_pokusov == 1 else 'Thanks for playing.'
    if pocet_pokusov < 10:
        odpoved += " You didn't need many trials, buddy. Thumbs up!"
    if pocet_pokusov >= 10:
        odpoved += " Not your best day today, hm?"
    return odpoved

def vyhodnot_cas(in_seconds):
    '''Podla potrebneho casu na uhadnutie vytvori odpoved.'''
    if in_seconds <= 60:
        msg = 'Great play! You needed only {} seconds to win.'.format(in_seconds)
    elif in_seconds <= 120:
        msg = 'Definitely not Flash Gordon but you seem to be pretty fast as well. Your time was {} min, {} sec.'.format(in_seconds // 60, in_seconds % 60)
    else:
        minutes = in_seconds // 60
        seconds = in_seconds % 60
        msg = 'You needed {} minutes and {} seconds to guess the secret number. No comment.'.format(minutes, seconds)
    return msg

# Vygenerovanie nahodneho stvorcisla
cisla = [str(a) for a in range(10)]
random.shuffle(cisla)
tajne = ('').join(cisla[:4])

print('Hi there!')
print('I\'ve generated a random 4-digit number for you.')
print('Let\'s play a bulls and cows game.')
print('Enter a number:')

number_of_guesses = 0

start_time = time()

while True:
    tip = input('>>> ')
    number_of_guesses += 1
    if tip == tajne:
        end_time = time()
        delta_time = round(end_time - start_time, 2)
        print('Correct, you\'ve guessed the right number in {} {}!'.format(number_of_guesses, 'guess' if number_of_guesses == 1 else 'guesses'))
        print(vyhodnot(number_of_guesses))
        print(vyhodnot_cas(delta_time))
        sys.exit()

    s1, s2 = cow_bull(tip, tajne)
    print('{}, {}'.format(s1, s2))
