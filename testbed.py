import math
import datetime 
import time

start = datetime.datetime.now()

while True:
    elapsed_ms = (datetime.datetime.now() - start) .total_seconds() * 1000
    brightness = int((math.exp(math.sin(elapsed_ms/2000.0*math.pi)) - 0.36787944) * 108.0)
    print (brightness)
    time.sleep(0.01)
