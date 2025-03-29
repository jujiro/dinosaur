from machine import Pin
import asyncio
from safe_dict import ThreadSafeDict
import time

wait_time_ns=100000000


async def evaluate_state():
    ms_bypass=pins_i[MS_BYPASS]["pin"]
    ms=pins_i[MS]["pin"]
    ls1=pins_i[LS1]["pin"]
    ls2=pins_i[LS2]["pin"]
    spst=pins_o[SPST_OUT]["pin"]
    dpdt=pins_o[DPDT_OUT]["pin"]
    if ms_bypass.value()==0 or ms.value()==1:
        spst.value(1)
        if ls1.value()==0 and dpdt.value()==1:
            dpdt.value(0)
        elif ls2.value()==0 and dpdt.value()==0:
            dpdt.value(1)    
    else:
        #Power off the motion
        spst.value(0)
        if ls1.value()==1 and dpdt.value()==1:
            dpdt.value(0)
        elif ls2.value()==1 and dpdt.value()==0:
            dpdt.value(1)
    #await print_output()
    

# Basic color codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  # This resets the color back to default

def format_colored_message(msg, color):
    return f"{color}{msg}{RESET}"

async def print_output():
    msg=format_colored_message("SPST", GREEN if pins_o[SPST_OUT]["pin"].value() else RED)
    msg+=", " + format_colored_message("DPDT", GREEN if pins_o[DPDT_OUT]["pin"].value() else RED)
    print(msg)
    
async def main():
    while True:        
        await evaluate_state()
        await asyncio.sleep(wait_time_ns / 1000000000)

LS1=18
LS2=19
MS_BYPASS=20
MS=21
SPST_OUT=16
DPDT_OUT=17

input_pins = [LS1,LS2,MS_BYPASS,MS]
output_pins = [SPST_OUT, DPDT_OUT]

irqs={
    LS1: Pin.IRQ_RISING, #Pin.IRQ_RISING | Pin.IRQ_FALLING,
    LS2: Pin.IRQ_RISING, #Pin.IRQ_RISING | Pin.IRQ_FALLING,
    MS_BYPASS: Pin.IRQ_RISING | Pin.IRQ_FALLING,
    MS: Pin.IRQ_RISING | Pin.IRQ_FALLING
}

pins_i=ThreadSafeDict()
pins_o=ThreadSafeDict()
#Wire all the input pins
for pin in input_pins:
    pins_i[pin]={}
    p0 = Pin(pin, Pin.IN)
    if irqs.get(pin, None):
        p0.irq(trigger=irqs[pin])
    pins_i[pin]["pin"]=p0

for pin in output_pins:
    pins_o[pin]={}
    p0 = Pin(pin, Pin.OUT)
    #p0.init(p0.IN, p0.PULL_DOWN)
    if pin==SPST_OUT:
        #p0.init(p0.OUT)
        p0.value(0)
    else:
        p0.value(1)
    pins_o[pin]["pin"]=p0

asyncio.run(main())