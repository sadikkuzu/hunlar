#! /usr/bin/python
# SADIK KUZU (c) 2020
# CS:GO config dosyalarini islemek icin arac gerecler

def t_nt(line):
    return str(line).replace('\t', ' ').replace('\n', '\t')

def t_(line):
    return str(line).replace('\t', ' ')

def n_(line):
    return str(line).replace('\n', ' ')

def sorgula(lines):
    sorgu_listesi = ["timestamp", "PlayersOnTeam", '"map"']
    for i in range(len(lines)):
        if "name" in lines[i]:
            if "disconnected" not in lines[i+1]:
                print(t_nt(lines[i]), t_(lines[i-2]), end='')
        if "HalfScore" in lines[i]:
            print(t_nt(lines[i]), n_(lines[i+2]), t_(lines[i+3]), end='')
        for sorgu in sorgu_listesi:
            if sorgu in lines[i]:
                print(t_(lines[i]), end='')
