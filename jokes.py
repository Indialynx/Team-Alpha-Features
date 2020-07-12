# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:58:16 2020

@author: kajal_m
#this is the code for random jokes display
"""
import time
import pyttsx3
engine = pyttsx3.init()

jokes = {"1":"Why do bees have sticky hair? Because they use honey combs!" ,
         "2":"What do you call a dinosaur that is sleeping? A dino-snore!" ,
         "3":"Why did the man run around his bed? Because he was trying to catch up on his sleep!" ,
         "4":"What did one plate say to the other plate? Dinner is on me!" ,
         "5":"What kind of tree fits in your hand? A palm tree!" ,
         "6":"How does a scientist freshen their breath? With experi-mints!" ,
         "7":"What do you call a dog magician? A labracadabrador" ,
         "8":"What do you call a funny mountain? Hill-arious"}

randomjoke = input("Enter the number for the joke which you would like to be displayed")
print(jokes[randomjoke])
engine.say(jokes[randomjoke])
engine.runAndWait()
time.sleep(3)

print("Hope you liked it")
    


