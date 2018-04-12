import sys
import time

sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("192.168.4.1", 6000,True)


bot.TurnOff("A", 2)
bot.TurnOff("A", 1)
bot.TurnOff("A", 3)
bot.TurnOff("A", 4)
bot.TurnOff("A", 5)
bot.TurnOff("A", 2)
bot.TurnOff("A", 1)
bot.TurnOff("A", 3)
bot.TurnOff("A", 4)
bot.TurnOff("A", 5)

i = 0;
def displayNumber(num):
    q = num;
    s = [16,8,4,2,1]
    index = 5

    for h in s:
        if(q >= h):
            q = q-h
            bot.TurnOn("A",index)
        else:
            bot.TurnOff("A",index)
        index -= 1


while True:
    displayNumber(i)
    time.sleep(0.5)
    i = (i + 1) % 32
