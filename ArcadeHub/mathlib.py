import math

def Sinwave(ypos, heightVar, ticks):
    sinTime = math.sin((ticks / 500) * 2 / math.pi) * (ypos / heightVar)
    y = ypos / 2 + sinTime
    return y