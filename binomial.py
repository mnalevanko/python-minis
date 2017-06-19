from math import factorial

def binomial(number_of_successes, number_of_trials, probability):

    kombinacne_cislo = factorial(number_of_trials) / (factorial(number_of_successes) * factorial(number_of_trials - number_of_successes))
    vysledok = kombinacne_cislo * probability**number_of_successes * (1 - probability)**(number_of_trials - number_of_successes)
    return vysledok


for a in range(4):
    print(binomial(a, 3, 0.5))
