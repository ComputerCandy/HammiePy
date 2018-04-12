import sys
import time
sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("192.168.4.1", 6000,True)


bot.TurnOn("A", 2)
bot.TurnOn("A", 1)
bot.TurnOn("A", 3)
bot.TurnOn("A", 4)
bot.TurnOn("A", 5)

while True:
    bot.Toggle("A",1)
    time.sleep(0.5)
    bot.Toggle("A",2)
    time.sleep(0.5)
    bot.Toggle("A",3)
    time.sleep(0.5)
    bot.Toggle("A",4)
    time.sleep(0.5)
    bot.Toggle("A",5)
    time.sleep(0.5)
