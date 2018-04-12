import sys
sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("192.168.4.1", 6000)
bot.sendRawNR("Hello!")
