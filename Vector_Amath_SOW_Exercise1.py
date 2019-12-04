import math

"""
    This exercisises is used to test understanding of Vectors. YOU are NOT to use any Numpy
    implementation for this exercises. 
"""

class Vector(object):
    """
        This class represents a vector of arbitrary size.
        You need to give the vector components. 
    """

    def __init__(self, components=None):
        self.__components=components
        """
            input: components or nothing
            simple constructor for init the vector
        """
        if components is None:
            components = []
        self.__components = list(components)


    def component(self, i):
        """
            input: index (start at 0)
            output: the i-th component of the vector.
        """
        if type(i) is int and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def __len__(self):
        """
            returns the size of the vector
        """
        return len(self.__components)

    def modulus(self):
        """
            returns the euclidean length of the vector
        """
        summe = 0
        for i in range(len(self.__components)):
            summe += (self.__components[i])**2
            
        return summe**0.5

    def add(self, other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the sum.
        """
        size = len(self)
        if size == len(other):
            for i,b in enumerate(other):
                self.__components[i] +=b
            return self.__components
        else:
            raise Exception("must have the same size")

    def sub(self, other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the difference.
        """
        size = len(self)
        if size == len(other):
            for i,b in enumerate(other):
                self.__components[i] -=b
            return self.__components
        else:  # error case
            raise Exception("must have the same size")

    def multiply(self, other):
        """
            multiply implements the scalar multiplication 
            and the dot-product
        """
        if isinstance(other, float) or isinstance(other, int): #scalar multiplication
            for i in range(len(self)):
                self.__components[i]= (self.__components[i])*other
            return self.__components
        elif isinstance(other, Vector) or (len(self.__components) == len(other)): # dot product
             summe = 0
             for i,b in enumerate(other):
                summe= summe + b*(self.__components[i])
             return summe
        
        else:  # error case
            raise Exception("invalid operand!")

    
    def scalar_proj(self, other):
        """ 
            Computes the scalar projection of vector r on s.
        """
        p1=self.multiply(other)
        p2=self.modulus()
        return p1/p2
        
    def vector_proj(self, other):
        """ 
            Computes the vector projection of vector r on s.
            use the other functions created above.
        """
        p1=self.multiply(other)
        p2=(self.modulus())**2
        return self.multiply(p1/p2)
    
    
v=Vector([1,2,3])
x=v.__len__()    
print("lenght of the vector is:",x)

print("the module is :", v.modulus())

print("the product of 2 vectors :",v.multiply([1,1,1]))

print("scalar_projection", v.scalar_proj([1,2,1]))

print("vector projection", v.vector_proj([1,2,1]))




