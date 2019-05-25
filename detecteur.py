#!/usr/bin/env python3
import RPi.GPIO as gpio
from time import time
from alerte_discord import send as discord_send
from communication_serveur_web import send as web_send
class Fenetre:
    def __init__(self,port,name):
        self.port=port
        self.name=name
        gpio.setup(port,gpio.IN)
        self.state=(not gpio.input(port))*time()
        selfdelay=1800
    def closing(self):
        if self.state and gpio.input(self.port):
            self.state=0.0
            return True
        return False
    def alert(self):
        if self.state+self.delay<=time() and self.delay and self.state:
            if self.delay==1800:
                self.delay=7200
                return "30 minutes"
            if self.delay==7200:
                self.delay=28800
                return "2 heures"
            if self.delay==28800:
                self.delay=0
                return "8 heures"
    def opening(self):
        if not (self.state or gpio.input(self.port)):
            self.state=time()
            self.delay=1800
            return True
        return False
gpio.setmode(gpio.BCM)
fenetres=[]
fenetres.append(Fenetre(14,"Fenetre 1"))
fenetres.append(Fenetre(15,"Fenetre 2"))
while 1: #boucle infine
    for fenetre in fenetres:
        #fermeture des fenetres
        if fenetre.closing():
            discord_send(fenetre.name+" fermee")
            web_send(fenetre.name,"closed")
        # alertes discord
        alert=fenetre.alert()
        if alert!=None:
            discord_send(fenetre.name+" ouverte depuis "+alert)
        #ouverture des fenetres
        if fenetre.opening():
            discord_send(fenetre.name+" ouverte")
            web_send(fenetre.name,"opened")
