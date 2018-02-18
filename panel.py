

class Panel:

    def __init__(self, strip, idx, pixels):
        print ('Panel initialized')
        self.idx = idx
        self.pixels = pixels
        self.strip = strip

    def setColor(self, c):

        for i in range(0, self.pixels):
            self.strip.setPixelColor(self.idx*self.pixels+i, c)



        
    