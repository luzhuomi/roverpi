
import piface.pfio
from time import sleep

class Rover:
    
    def __init__(self):
        piface.pfio.init()
        
    def forward(self,unit=0.5):
        piface.pfio.digital_write(1, 1)
        piface.pfio.digital_write(2, 1)
        sleep(unit)
        piface.pfio.digital_write(1, 0)
        piface.pfio.digital_write(2, 0)

    def right(self,unit=0.5):
        piface.pfio.digital_write(1, 0)
        piface.pfio.digital_write(2, 1)
        sleep(unit)
        piface.pfio.digital_write(1, 0)
        piface.pfio.digital_write(2, 0)

    def left(self,unit=0.5):
        piface.pfio.digital_write(1, 1)
        piface.pfio.digital_write(2, 0)
        sleep(unit)
        piface.pfio.digital_write(1, 0)
        piface.pfio.digital_write(2, 0)
