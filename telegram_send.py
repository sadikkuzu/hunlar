#! /usr/bin/python3
# SADIK KUZU (c) 2020

try:
    import telepot
    from telegram_credentials import hun, csgo
    from araclar import simdi
except:
    import sys
    sys.exit('There aint any required package(s).')

def hunlar():
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

if __name__ == "__main__":
    hunlar()