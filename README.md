# i2c_slave_micropython_noise
This is the MicroPython version of my [i2c_slave_fpga_noise repo](https://github.com/charkster/i2c_slave_fpga_noise). Instead of using a fpga to mimic noise, a MCU running MicroPython can instead be used.

i2c_slave_change_address.py should be renamed to main.py and saved to the MCU's flash (using Thonny or your favorite MicroPython IDE). 

This simple code will have the slave address change on the 5th completed read or write cycle. This mimics I2C bus noise where the expected slave does not give a NACK, even when the I2C master sends a correct slave address. 

This feature is useful when testing a bench setup to see if it can handle a missing NACK without halting the evaluation of the system.
