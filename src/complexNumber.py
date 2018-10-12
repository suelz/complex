
class complexNumber(object):

    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def getReal(self):
        return self.real

    def getImag(self):
        return self.imag

    def __add__(self, x):
        return complexNumber(self.real + x.real, self.imag + x.imag)

    def __sub__(self, x):
        return complexNumber(self.real - x.real, self.imag - x.imag)

    def __mul__(self, x):
        return complexNumber(self.real * x.real - self.imag * x.imag, self.imag*x.real + self.real * x.imag)

    
    def __str__(self):
        return('%g, %gi') % (self.real, self.imag)
