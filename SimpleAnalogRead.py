import pyfirmata
import time
PINS = (0, 1, 2, 3)
board = pyfirmata.Arduino('/dev/ttyACM0')
print("Setting up the connection to the board ...")
it = pyfirmata.util.Iterator(board)
it.start()
for pin in PINS:
    board.analog[pin].enable_reporting()
while True:
    for pin in PINS:
        print("Pin %i : %s" % (pin, board.analog[pin].read()))
        time.sleep(2)
    while board.analog[0].read>=0:
        print("Hello")
        
