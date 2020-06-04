#! /usr/bin/python
# SADIK KUZU (c) 2020
# parametresiz calisir. direkt ara dosyadan (tmp) okur ve isler.

import araclar as ar

lines = []
folder = "/home/csgo/csgo/csgo/"
hun = "backup_round00.txt"
hun = folder + hun


try:
    tmp = "/root/hunlar/kimler-oynuyor-simdi.tmp"
    f = open(tmp, 'r')
    satir = f.readline()
    print(satir, end='')
    hun = folder + str(satir.split()[-1])
except:
    pass


# print(hun)
f = open(hun, 'r')
lines = f.readlines()

sorgu_listesi = ["timestamp", "PlayersOnTeam", '"map"']


def sorgula0():
    for line in lines:
        for sorgu in sorgu_listesi:
            if sorgu in line:
                print(line, end='')


def sorgula():
    for i in range(len(lines)):
        if "name" in lines[i]:
            if "disconnected" not in lines[i+1]:
                print(lines[i].replace('\t', ' ').replace('\n', '\t'), lines[i-2].replace('\t', ' ') ,end='')
        if "HalfScore" in lines[i]:
            print(lines[i].replace('\t', ' ').replace('\n', '\t'), lines[i+2].replace('\n', ' '), lines[i+3].replace('\t',' ') ,end='')
        for sorgu in sorgu_listesi:
            if sorgu in lines[i]:
                print(lines[i].replace('\t', ' '), end='')


if __name__ == "__main__":
    ar.sorgula(lines)
