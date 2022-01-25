'''
@file       main.py
@brief      Main file that runs tasks cooperatively
@author     Cesar Santana
@author     Jacob Frabosilio
@author     Ayden Carbaugh
'''
import motor_driver
import pyb
import encoder_driver

## Initializes encoder_driver.py
enc = encoder_driver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.B6), pyb.Pin(pyb.Pin.cpu.B7), pyb.Timer(4, prescaler = 0, period = 65535))

## Initializes motor_driver.py
moe = motor_driver.MotorDriver(pyb.Pin(pyb.Pin.cpu.A10), pyb.Pin(pyb.Pin.cpu.B4), pyb.Pin(pyb.Pin.cpu.B5), pyb.Timer(3, freq = 20000))

if __name__ == '__main__':
    while True:
        
        moe.set_duty_cycle(-50)
        enc.read()
        print(enc.pos)
        
