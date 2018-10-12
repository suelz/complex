import math

class complexNumber(object):

    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return('%g, %gi') % (self.real, self.imag)
    
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

    def __truediv__(self, x):
        d = abs(x) ** 2
        real = self.real * x.real + self.imag * x.imag
        imag = self.imag * x.real - self.real * x.imag
        return complexNumber(real/d, imag/d)

    def __abs__(self):
       return math.sqrt(self.real**2 + self.imag**2)

    def __neg__(self):
       return complexNumber(-self.real, -self.imag)

    def conj(self):
        return complexNumber(self.real, -self.imag)

    def __eq__(self, x):
        return self.real == x.real and self.imag == x.imag

    def __ne__(self, x):
        return not self.__eq__(x)

