#!/usr/bin/env python3
import rpi.GPIO as gpio
from time import time
from alerte_discord import send as discord_send
from communication_serveur_web import send as web_send
gpio.setmode(gpio.BCM)
PORT_FNT1=14
PORT_FNT2=15
gpio.setup(PORT_FNT1,gpio.IN)
gpio.setup(PORT_FNT2,gpio.IN)
state1=(not gpio.input(PORT_FNT1))*time()
state2=(not gpio.input(PORT_FNT2))*time()
delay1=1800
delay2=1800
while 1: #boucle infine
    #fermeture des fenetres
    if state1 and gpio.input(PORT_FNT1):
        state1=0.0
        discord_send("Fenetre 1 fermée")
        web_send(1,"close")
    if state2 and gpio.input(PORT_FNT2):
        state2=0.0
        discord_send("Fenetre 2 fermée")
        web_send(2,"close")
    # alertes discord 
    if state1+delay1<=time() and delay1!=0 and state1:
        if delay1==1800:
            discord_send("Fenetre 1 ouverte depuis 30 minutes")
            delay1=7200
        elif delay1==7200:
            discord_send("Fenetre 1 ouverte depuis 2 heures")
            delay1=28800
        elif delay1==28800:
            discord_send("Fenetre 1 ouverte depuis 8 heures")
            delay1=0
    if state2+delay2<=time() and delay2!=0 and state2:
        if delay2==1800:
            discord_send("Fenetre 2 ouverte depuis 30 minutes")
            delay2=7200
        elif delay2==7200:
            discord_send("Fenetre 2 ouverte depuis 2 heures")
            delay2=28800
        elif delay2==28800:
            discord_send("Fenetre 2 ouverte depuis 8 heures")
            delay2=0
    #ouverture des fenetres
    if not (state1 or gpio.input(PORT_FNT1)):
        state1=time()
        discord_send("Fenetre 1 ouverte")
        web_send(1,"open")
        delay1=1800
    if not (state2 or gpio.input(PORT_FNT2)):
        state2=time()
        discord_send("Fenetre 2 ouverte")
        web_send(2,"open")
        delay2=1800
