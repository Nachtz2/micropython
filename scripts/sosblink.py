#Lara 1/20
#We made the pico LED light turn on and off for a certain amount of time

from include.rcc_library import Raft 
import utime 

myraft = Raft ()

myraft. led_on () 
utime.sleep_ms(1000)
myraft.led_off()
