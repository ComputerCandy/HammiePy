import sys
sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("127.0.0.1", 1234)
bot.AllOff("A")
bot.TurnOn("A", 1)
bot.TurnOff("A", 1)
bot.Toggle("A",1)
bot.AllOn("A")
