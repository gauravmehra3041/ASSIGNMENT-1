import math
346
pie = 3.14
i = 0
for i in range(0,346,15) :
    x = math.sin(math.radians(i))
    y = math.cos(math.radians(i))
    print( i , " --- " ,round(x,4),round(y,4))

