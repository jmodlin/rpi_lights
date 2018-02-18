

class Panel:

    def __init__(self, strip, idx, pixels):
        print ('Panel initialized')
        self.strip = strip
        self.idx = idx
        self.pixels = pixels

    def setColor(self, c):
        for i in range(self.idx*i, self.idx*i+pixels):
            self.strip.setPixelColor(i, c)


        
    