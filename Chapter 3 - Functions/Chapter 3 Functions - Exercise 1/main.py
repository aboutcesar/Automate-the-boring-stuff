# This is a program that will print out zig-zags

import sys, time

indent = 0
increaseIndent = True

try:
    while True:
        print(' ' * indent, end = '')
        print("*******")
        time.sleep(.01)

        if increaseIndent:
            indent += 1
            if indent == 20:  #number of spaces for the indent will be 20 then it will start to decrease
                increaseIndent = False
        else:
            indent -= 1
            if indent == 0:
                increaseIndent = True
except KeyboardInterrupt:
    sys.exit()
