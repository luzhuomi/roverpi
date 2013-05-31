roverpi
=======

a simple implementation of a rover using raspberry pi and PiFace


prerequisite
============
https://github.com/thomasmacpherson/piface

OS
==
Raspbian

demo
====
```
pi@raspberrypi ~/git/roverpi/trunk/roverpi $ sudo modprobe spi_bcm2708
pi@raspberrypi ~/git/roverpi/trunk/roverpi $ sudo python
Python 2.7.3 (default, Jan 13 2013, 11:20:46) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import rover as r
>>> x = r.Rover()
>>> x.forward()
>>> x.right()
>>> x.left()
```
