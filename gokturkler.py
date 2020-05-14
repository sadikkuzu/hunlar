#! /usr/bin/python
# SADIK KUZU (c) 2020
# parametre ile dosya adi alir
# ornek:
# python3.8 ~/hunlar/gokturkler.py /home/csgo/csgo/csgo/backup_round07.txt

import sys
import araclar as ar

folder = "/home/csgo/csgo/csgo/"
hun = "backup_round00.txt"
fullhun = folder + str(hun)


try:
	for madde in sys.argv:
		print(madde, end=' ')
	print("")
	if "backup_round" in sys.argv[-1]:
		hun = sys.argv[-1]
except:
	pass

if "csgo/" in hun:
	fullhun = str(hun)
else:
	fullhun = folder + str(hun)


print(fullhun)
f = open(fullhun, 'r')
lines = f.readlines()


ar.sorgula(lines)
