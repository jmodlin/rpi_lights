

class Panel:

    def __init__(self, strip, idx, pixels):
        print ('Panel initialized')
        self.strip = strip
        self.idx = idx
        self.pixels = pixels

    def setColor(self, c):

        for i in range(0, self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)


        
    