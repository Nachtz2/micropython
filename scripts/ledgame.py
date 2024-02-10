#Lara 1/20
#This code was to turn picos light on as well

from include.rcc_library import Raft

myraft = Raft() 

favcolor = "blue"
age=24

if favcolor == "blue" and age > 13:
    myraft.led_on() 