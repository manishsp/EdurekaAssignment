# 3. Weather forecasting organization wants to show is it day or night. So, write a
# program for such organization to find whether is it dark outside or not.
# Hint: Use time module.

import time


def dayornight(x, y):
    if x >= 18 or x <= 6:
        print(f"Current time is {x}:{y} and its dark outside")
    else:
        print(f"Current time is {x}:{y} and its not dark outside yet")


hour = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
dayornight(hour, minutes)
