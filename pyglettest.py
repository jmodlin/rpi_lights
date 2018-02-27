import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'silent')

march = pyglet.media.load('/home/pi/Documents/rpi_porch/rpi_lights/Game_Room.mp3')
march.play()

