# Environment and Goals
* Connect RasPi with Arduino
* Exchange (Sensor)data between both
  * Arduino has ADC to read out analoge sensors
* Use of Rust for Raspi-programming

# Software
* Own RustPiIO library for RasPi
* C++ for Arduino

# RasPi Configuration
* turn on I²C with the raspi-config

# Wireing
* use of Level Shifter is advised
  * Pi is 3.3V device but arduino is 5V
  * although nothing explodes if you do not
* USE THE RIGHT PINS!!!! For your own times sake! 
  * I²C-EEPROM-Pins ≠ I²C-Pins 
  * The basic I²C Pins on the RasPi are the ones that are activated with the raspi config

# References
[I²C Specs](http://www.i2c-bus.org/fileadmin/ftp/i2c_bus_specification_1995.pdf)  
[SMBus Specs](http://www.smbus.org/specs/smbus20.pdf)  
[Forum thread](https://www.raspberrypi.org/forums/viewtopic.php?t=193050) which indicates that the SMBus protocoll is not implemented in the Arduino [Wire](https://www.arduino.cc/en/Reference/Wire) library  
