#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

#-----------------------------------------------------------------------------
import itertools 

def fib(n):
    # if n = 0, return n
    # if n = 1, return n
    # if n > 1, return fib(n-1) + fib(n-2)
    if n is 0 or n is 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#-----------------------------------------------------------------------------

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "V2[" + str(self.x) + ", " + str(self.y) + "]"

    def getX(self):
        print self.x

    def getY(self):
        print self.y

    def __add__(self, vector):
        return self.add(vector)

    def add(self, vector):
        return V2(self.x + vector.x, self.y + vector.y)

    def __mul__(self, vector):
        return self.mul(vector)

    def mul(self, vector):
        return V2(self.x * vector, self.y * vector)


#Define a Python class V2, which represents two-dimensional vectors and
#supports the following operations:
# Create a new vector out of two real numbers: v = V2(1.1, 2.2)
# Convert a vector to a string (with the __str__ method)
# Access the components (with the getX and getY methods)
# Add two V2s to get a new V2 (with add and __add__ methods)
# Multiply a V2 by a scalar (real or int) and return a new V2 (with the mul
#and __mul__ methods)
#-----------------------------------------------------------------------------

class Polynomial:
    # class Polynomial takes "self and list" as parameter
    def __init__(self, coefficients):
        self.coeffs = []
        self.length = 0
        for num in coefficients:
            self.coeffs.append(num * 1.0)
            self.length += 1

    def coeff(self, i):
        pos = self.length - i - 1
        return self.coeffs[pos]

    def add(self, other):
        self.added = []
        for item in itertools.izip_longest(reversed(self.coeffs), reversed(other.coeffs), fillvalue=0):
            self.added.insert(0, (item[0] + item[1]))

        return Polynomial(self.added)

    def __add__(self, other):
        return self.add(Polynomial(other.coeffs))

    def mul(self, other):
        self.mult1 = []
        self.mult2 = []
        for item in itertools.izip_longest(reversed(self.coeffs), reversed(other.coeffs), fillvalue=1):
            self.mult1.insert(0, (item[0] * item[1]))

        for i in range(0, (self.length * 2 - 1)):
            self.mult2.append(0)

        for item in self.mult1:
            self.mult2[self.mult1.index(item) * 2] = item

        return Polynomial(self.mult2)

    def __mul__(self, other):
        return self.mul(Polynomial(other.coeffs))

    def __str__(self):
        string = ""
        for i in range (0, self.length):
            if self.coeffs[i] != 0.0:
                if (self.length - (i+1)) > 1:
                    string += str(self.coeffs[i]) + " z**" + str(self.length - (i+1)) + " + "
                elif (self.length - (i+1)) is 1:
                    string += str(self.coeffs[i]) + " z"  + " + "
                elif (self.length - (i+1)) is 0:
                    string += str(self.coeffs[i])
        return string

    def val(self, v):
        total = 0
        for i in range (0, self.length):
            total += self.coeffs[i] * v**(self.length - (i+1))
        return total

    def roots(self):
        root_list = []
        if self.length > 3:
            return "Order too high to solve for roots."
        else:
            if self.length == 1:
                return "Does not have any roots."
            elif self.length == 2:
                return (0 - self.coeffs[1]) / self.coeffs[0]
            elif self.length == 3:
                a = self.coeffs[0]
                b = self.coeffs[1]
                c = self.coeffs[2]

                under_root = b**2 - (4 * a * c)
                denominator = 2 * a

                if under_root >= 0:
                    numerator1 = (-1 * b) + under_root**0.5
                    numerator2 = (-1 * b) - under_root**0.5
                else:
                    numerator1 = (-1 * b) + complex(under_root, 0)**0.5
                    numerator2 = (-1 * b) - complex(under_root, 0)**0.5
                return [(numerator1 / denominator), (numerator2 / denominator)]

    def __repr__(self):
        return str(self)





p1 = Polynomial([1, 2, 3])
p2 = Polynomial([1, 2])
p3 = Polynomial([3, 2, -1])
p4 = Polynomial([4, 3, 2, 1])

print p1














