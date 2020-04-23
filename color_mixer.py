from phySyncFirmata import ArduinoNano, util
import time
board = ArduinoNano('COM3')

it = util.Iterator(board)
it.start()

board.analog[2].enable_reporting()
board.analog[3].enable_reporting()
board.analog[4].enable_reporting()

#declaring digital LED pins to be used as PWM
Rled = board.get_pin('d:10:p')
Gled = board.get_pin('d:9:p')
Bled = board.get_pin('d:6:p')

while True:
    Rled.write(board.analog[2].read()) #value of pot is directly controlling intensity of LEDs 
    Gled.write(board.analog[3].read())
    Bled.write(board.analog[4].read())
    board.pass_time(0.1)