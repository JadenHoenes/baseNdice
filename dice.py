#!/usr/bin/env python3
from random import randint

lst = {
    'num_dice' : ['Enter the number of dice you would like to roll: ', None],
    'num_side': ['Enter the number of sides you want your dice to have: ', None]
}
bN = 0
rbase='n'
obase='n'
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def setup():
    global bN
    global rbase
    global obase
    bd = input('Use decimal system? (y/n): ')
    if 'n' in bd:
        loo = True
        while loo:
            try:
                bN = int(input('(1-36) base = '))
                if bN < 1 or bN > 36:
                    a = int('a')
                loo = False
            except:
                print('You must use a number between 1 and 36!')

        rbase = input('base N dice rolls? (y/n): ')
        obase = input('output as base N? (y/n): ')

def base_encode(number, base):
    global alpha
    baseval = ''

    if 0 <= number < base:
        return alpha[number]

    while number != 0:
        number, i = divmod(number, base)
        baseval = alpha[i] + baseval

    return baseval

def get_num_dice():
    global lst
    global bN
    for x in lst:
        if 'n' in rbase:
            xin = input(lst[x][0])
            xin = int(xin)
            lst[x][1] = xin
        else:
            lue = True
            while lue:
                try:
                    xin = input(lst[x][0])
                    total = int(xin, bN)+1
                    it = 0
                    lst[x][1] = total
                    lue = False
                except:
                    print('You entered a value not available in your current base! Valid values are 0-'+alpha[bN-1])

def roll(i, num_side):
    rolls = []
    for x in range(i):
        if 'n' in obase:
            rolls.append(randint(1, num_side))
        else:
            rolls.append(base_encode(randint(1, num_side), bN))
    return rolls

setup()
get_num_dice()

roll = roll(lst['num_dice'][1], lst['num_side'][1])
with open('rolls.txt', 'w+') as f:
    f.write(', '.join(str(e) for e in roll))
