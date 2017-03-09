from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    x = 0.0
    y = 0.0

    #account for left side of drawing by swapping
    if x0 <= x1:
        x = x0
        y = y0
    else:
        x = x1
        x1 = x0
        y = y1
        y1 = y0



    A = y1 - y
    B = -(x1 - x)
    
    if x == x1:
        if y < y1:
            while y <= y1:
                plot(screen, color, x, y)
                y += 1
        else:
            while y >= y1:
                plot(screen, color, x, y)
                y -= 1
        return
        #some shit
    
    slope = float(y1 - y)/float(x1 - x)
    
    if slope > 1.0: #oct 2
        d = (2 * B) + A
        A *= 2; B *= 2
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += A
            y += 1
            d += B
    elif slope >= 0.0:
        d = (2 * A) + B
        A *= 2; B *= 2
        while x <= x1: #oct 1
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += B
            x += 1
            d += A
    elif slope >= -1.0: #oct 8
        d = (2 * A) - B
        A *= 2; B *= 2
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= B
            x += 1
            d += A
    elif slope < 1.0: #oct 7
        d = A - (2 * B)
        A *= 2; B *= 2
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += A
            y -= 1
            d -= B

'''
        
def draw_line_oct1( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = (2 * A) + B
    A *= 2
    B *= 2
    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += B
        x += 1
        d += A

def draw_line_oct2( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = (2 * B) + A
    A *= 2
    B *= 2
    print "x: " + str(x) + ", y: " + str(y)
    print "x1: " + str(x1) + ", y1: " + str(y1)

    while y <= y1:
        plot(screen, color, x, y)
        print "x: " + str(x) + ", y: " + str(y)
        if d < 0:
            x += 1
            d += A
        y += 1
        d += B

def draw_line_oct8( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = (2 * A) - B
    A *= 2
    B *= 2
    while x <= x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= B
        x += 1
        d += A

def draw_line_oct7( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = A - (2 * B)
    A *= 2
    B *= 2
    print "x: " + str(x) + ", y: " + str(y)
    print "x1: " + str(x1) + ", y1: " + str(y1)

    while y >= y1:
        plot(screen, color, x, y)
        print "x: " + str(x) + ", y: " + str(y)
        if d > 0:
            x += 1
            d += A
        y -= 1
        d -= B
'''
