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
    
    rgb = tuple(map(ord,hex(color)[2:].zfill(6).decode('hex')))
    return rgb
 
def rgb2color(rgb):
    color = Color(rgb[0], rgb[1], rgb[2])
    return color
 
def color_run(start_color, end_color, step_count, inclusive=True, to_colors=True):
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
    print('startColor =>'),
    print startColor
    endColor = color2rgb(end_color)
    print('endColor =>'),
    print endColor

    stepR = ((startColor[0] - endColor[0])/(step_count*-1.0)) if startColor[0] >= endColor[0] else ((endColor[0] - startColor[0])/(step_count*1.0))
    stepG = ((startColor[1] - endColor[1])/(step_count*-1.0)) if startColor[1] >= endColor[1] else ((endColor[1] - startColor[1])/(step_count*1.0))
    stepB = ((startColor[2] - endColor[2])/(step_count*-1.0)) if startColor[2] >= endColor[2] else ((endColor[2] - startColor[2])/(step_count*1.0))

    print 'stepR ->' + `stepR`
    print 'stepG ->' + `stepG`
    print 'stepB ->' + `stepB`

    # Create run as array of RGB tuples
    run = []
    for s in range(1, step_count+1):
        c = (startColor[0]+int(s*stepR), startColor[1]+int(s*stepG), startColor[2]+int(s*stepB))
        run.append(c)
    
    if inclusive:
        run = [startColor] + run + [endColor]
    print 'run->'
    print run

    # Convert tuples array to array of color objects
    if to_colors:
        colors = []
        for c in run:
            colors.append(Color(c[0], c[1], c[2]))
        return colors
    else:
        return run
   
# Main program logic follows:
if __name__ == '__main__':
 
    print 'color2rgb (255,0,0)-> ',
    rgb = color2rgb(Color(255,0,0))
    print rgb
 
    print 'rgb2color -> ',
    c = rgb2color(rgb)
    print c
 
    colors = color_run(Color(255,0,0), Color(0,212,255), 10, True)
    print 'color_run ->'
    print colors
 
    colors = color_run(Color(255,0,0), Color(255,0,255), 100, True)
    print 'color_run ->'
    print colors

    #  color_merge -> None - Do nothing, the color in this effect should be left alone
    #                 MergeBlack - If this effect has black pixels, merge them with effect color below
    #                 MergeAll - Merge all pixes with effect color below
    #                 ReplaceBlack - If this effect has black pixels, replace them with effect color below
    #
    # { title: 'Rachael Carson Bridge', 
    #   tick_ms: 100, 
    #   sound_file: '',
    #   effects: [
    #       { effect: 'background', 
    #           tick_start: 0,
    #           tick_end: 0,
    #           z_index: 0, 
    #           color_merge: None,
    #           panels: [p for p in range(24)],
    #           effect_params: {colors: [0], rocker: False}
    #       },
    #       { effect: 'streak', 
    #           tick_start: 0,
    #           tick_end: 0,
    #           z_index: 10,
    #           color_merge: None,
    #           panels: [] 
    #           effect_params: {colors: [0], rocker: False},
    #       }]
    # }
    #
    #
   
