import sys
import time
sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("192.168.4.1", 6000,True)


bot.TurnOn("A", 1)
bot.GetPinState("A",1)
