

class Panel:

    def __init__(self, idx, pixels):
        print ('Panel initialized')
        self.idx = idx
        self.pixels = pixels

    def setColor(self, strip, c):

        for i in range(0, self.pixels):
            strip.setPixelColor(self.idx*self.pixels+i, c)
            print (self.idx*self.pixels+i)


        
    