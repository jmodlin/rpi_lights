import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'silent')

march = pyglet.media.load('Game_Room.mp3')
march.play()

