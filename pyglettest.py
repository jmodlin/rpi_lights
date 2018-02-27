import pyglet

pyglet.options['audio'] = ('openal', 'pulse', 'silent')

march = pyglet.media.load('/media/share/Game_Room.mp3')
march.play()

