class Cplx:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex
    def __add__(self,other):
        return Cplx(self.real + other.real, self.complex + other.complex) 
    def __sub__(self,other):
        return Cplx(self.real - other.real, self.complex - other.complex)
    def __repr__(self):
        return f"{self.real} + {self.complex}i"
    
z1 = Cplx(5,3)
z2 = Cplx(1,2)

print(z1+z2)

