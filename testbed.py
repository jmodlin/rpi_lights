import math
import datetime 
import time
import os
import errno
from neopixel import *

start = datetime.datetime.now()

def color_run(start_color, end_color, step_count, inclusive=True, to_color=True):
    """
    Given a start color, end color, and a number of steps, returns a list of colors which represent a 'scale' between
    the start and end color.
    :param start_color: The color starting the run
    :param end_color: The color ending the run
    :param step_count: The number of colors to have between the start and end color
    :param inclusive: Flag determining whether to include start and end values in run (default True)
    :param to_color: Flag indicating return values should be Color objects (default True)
    :return: List of colors between the start and end color
    :rtype: list
    """
    #if isinstance(start_color, Color):
    #    start_color = start_color.rgb

    #if isinstance(end_color, Color):
    #    end_color = end_color.rgb

    step = tuple((end_color[i] - start_color[i])/step_count for i in range(3))

    add = lambda x, y: tuple(sum(z) for z in zip(x, y))
    mult = lambda x, y: tuple(y * z for z in x)

    run = [add(start_color, mult(step, i)) for i in range(1, step_count)]

    if inclusive:
        run = [start_color] + run + [end_color]

    #return run if not to_color else [Color(c) for c in run]
    return run


def colorMerging():
    print ('Color merging ...')
    colors = color_run((255,0,0), (0, 212, 255), 200)
    print colors


def pipetest():
    print ('Begining pipetest function ...')
    try: os.mkfifo('/tmp/lights',0777)
        except OSError: 
            print 'error!'
    bufferSize = 100
    PATH = "/tmp/lights"
    while True:
        try:
            pipe = os.open(PATH, os.O_RDONLY | os.O_NONBLOCK)
            input = os.read(pipe,bufferSize)
        except OSError as err:
            if err.errno == 11:
                continue
            else:
                raise err
        if input:
            print(input)
    
        os.close(pipe)
    
        #Other functions
        print "Sleep 500 ms"
        time.sleep(0.5)

# Call test procedures
pipetest()