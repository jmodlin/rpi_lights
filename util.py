# Stock libraries
import time
import random
import signal
import sys
import math
import datetime
 
# Custom objects
from neopixel import *
from panel import *
from animation import *
from display import *
 
def color2rgb(color):
    rgb = tuple(map(ord,hex(color)[2:].decode('hex')))
    return rgb
 
def rgb2color(rgb):
    color = Color(rgb[0], rgb[1], rgb[2])
    return c
 
def color_run(start_color, end_color, step_count, inclusive=True):
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
 
    # Convert color value to RGB tuple
    startColor = color2rgb(start_color)
    endColor = color2rgb(end_color)
 
    step = tuple((endColor[i] - startColor[i])/step_count for i in range(3))
    add = lambda x, y: tuple(sum(z) for z in zip(x, y))
    mult = lambda x, y: tuple(y * z for z in x)
 
    # Create run as array of RGB tuples
    run = [add(startColor, mult(step, i)) for i in range(1, step_count)]
 
    if inclusive:
        run = [startColor] + run + [endColor]
 
    # Convert tuples array to array of color objects
    colors = []
    for c in run:
        colors.append(Color(c[0], c[1], c[2]))
 
    return colors
 
   
# Main program logic follows:
if __name__ == '__main__':
 
    print 'color2rgb (255,0,0)-> ',
    rgb = color2rgb(Color(255,0,0))
    print rgb
 
    print 'rgb2color -> ',
    c = rgb2color(rgb)
    print c
 
    colors = color_run(Color(255,0,0), Color(0,212,255), 253)
    print 'color_run ->'
    print colors
 
   
