import sys
sys.path.insert(0, '../src/')
from hammie import *

bot = Hammie("127.0.0.1", 1234)
bot.sendRawNR("Hello!")
