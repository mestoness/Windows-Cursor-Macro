import win32api
import math
import time
from random import randint

for i in range(9000009909909009099999999):
    x = int(500+math.sin(math.pi*i/100)*500)
    y = int(randint(300,500)+math.cos(i)*150)
    win32api.SetCursorPos((x,y))
    time.sleep(.12)
