from machine import Pin, PWM

pin = 9 #number for gpio pin

pwm_pin = PWM(Pin(pin))
#frequency is Cycles per second (Hertz, Hz)
pwm_pin.freq(10)#Hz

percent = 50

pwm_pin.duty_u16(percent*655)