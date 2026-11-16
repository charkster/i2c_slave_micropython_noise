import machine

i2c_slave = machine.I2CTarget(addr=0x70, sda=machine.Pin(6), scl=machine.Pin(7)) # RP2350 XIAO
count = 0

def irq_handler(i2c_target):
    global count
    global i2c_slave
    count += 1
    if (count % 5 == 0): # every 5th access change the slave address to 0import x71
        i2c_slave.deinit()
        i2c_slave = machine.I2CTarget(addr=0x71, sda=machine.Pin(6), scl=machine.Pin(7))
    else: # change back if not the 5th access
        i2c_slave.deinit()
        i2c_slave = machine.I2CTarget(addr=0x70, sda=machine.Pin(6), scl=machine.Pin(7))
    triggers = ( machine.I2CTarget.IRQ_END_READ | machine.I2CTarget.IRQ_END_WRITE )
    i2c_slave.irq(irq_handler, trigger=triggers, hard=False)

triggers = ( machine.I2CTarget.IRQ_END_READ | machine.I2CTarget.IRQ_END_WRITE )
i2c_slave.irq(irq_handler, trigger=triggers, hard=False)