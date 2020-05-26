#! /usr/bin/python
# SADIK KUZU (c) 2020

import telepot
from telegram_credentials import hun, csgo
from araclar import simdi

bot = telepot.Bot(hun)

f = open(simdi, 'r')
data = f.readlines()
tire = '---------------------------------------------------------------------------\n'
tire2 = '===========================================================================\n'
while tire in data:
    data.remove(tire)
while tire2 in data:
    data.remove(tire2)
dat = ''.join(data)
msj = dat.strip()
resp = bot.sendMessage(csgo, msj)
