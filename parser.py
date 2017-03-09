
from transform import *
from display import *
from matrix import *
from draw import *
from time import sleep

def parse_file(fname, points, transform, screen, color):
    f = open(fname, 'r')
    lines = f.readlines()
    i = 0
    while i < len(lines):
        cmd = lines[i].strip()
        print(cmd + " - " + str(i))
#        try:
        if cmd == "line":
            print(cmd)
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            points = add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            i += 2
        elif cmd == "ident":
            print(cmd)
            transform = identity_mtrx()
            i += 1
        elif cmd == "scale":
            print(cmd)
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            transform = scale(transform, args[0], args[1], args[2])
            i += 2
        elif cmd == "move":
            print(cmd)
            args = lines[i+1].strip().split()
            for k in range(len(args)):
                args[k] = float(args[k])
            transform = translate(transform, args[0], args[1], args[2])
            i += 2
        elif cmd == "rotate":
            print(cmd)
            args = lines[i+1].strip().split()
            if args[0] == "x":
                transform = rotateX(transform, float(args[1]))
            elif args[0] == "y":
                transform = rotateY(transform, float(args[1]))
            elif args[0] == "z":
                transform = rotateZ(transform, float(args[1]))
            else:
                raise Exception("not an axis, try again")
            i += 2
        elif cmd == "apply":
            print(cmd)
            display_mtrx(transform)
            print("APPLY:")
            points = mtrx_mult(points, transform)
            i += 1
        elif cmd == "display":
            sleep(1)
            print(cmd)
            draw_lines(screen, points, color)
            display(screen)
            i += 1
        elif cmd == "save":
            display_mtrx(points)
            display
            arg = lines[i+1].strip()
            draw_lines(screen, points, color)
            save_extension(screen, arg)
            i += 2
        elif cmd == "quit":
            return
        else:
            print(cmd)
            raise Exception("invalid command")
#        except:
#            print "invalid file to parse. please edit and try again"
            
