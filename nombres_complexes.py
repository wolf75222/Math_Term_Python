#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# Romain.D 19/12/2021
# =============================================================================

from math import sqrt, degrees, atan, pi
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from fraction import *

# =============================================================================
#  i² = -1
#  forme algébrique : z = a+ib (avec a;b -> réel)
#  forme trigo : z = |z|cos(teta)+isin(teta) (avec teta = arg(z))
#  forme expo : e(iteta) = cos(teta) + i sin(teta), z = |z|e(iteta)
# =============================================================================

class NBcomplexe():
    """
    La class des nombres complexes""
        a : partie réel du nombre complexe
        b : partie imaginaire du nombre complexe
    """
    def __init__(self, x = 0, y = 0):  
        #J'implémenterai l'appel avec un nombre complexe en paramètre qui permet ainsi la copie d'instances
        #assert isinstance(x, int or float or Fraction), "Attribut 'x' : doit être de type float ou int"
        
        self.a = x
        self.b = y


    def __eq__(self,other): 
        """
        >>> NBcomplexe(1,2)==NBcomplexe(1,2)
        True
        >>> NBcomplexe(1,2)==NBcomplexe(1,3)
        False
        >>> NBcomplexe(1,0)==1
        True

        """
        if other.__class__ is NBcomplexe:
            x =(self.a==other.a and self.b==other.b )
        else:
            x = (self.a==other and self.b==0)
        return x 
        

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return f"0"
        if self.a == 0:
            return f"{self.b}i"
        if self.b == 0:
            return f"{self.a}"
        return f"{self.a} + {self.b}i"
    

    def __repr__(self):
        return f"NBcomplexe({self.a},{self.b})"#Modif GV
    
    def __add__(self, other):
        """
        >>> (2+NBcomplexe(1,2))+(NBcomplexe(1,2)+2)+(2-NBcomplexe(1,2))
        NBcomplexe(7,2)
        """
        if other.__class__ is NBcomplexe:
            x = self.a + other.a
            y = self.b + other.b
        else:
            x = self.a + other
            y = self.b 
        
        return NBcomplexe(x,y)


    def __radd__(self, other):
        return self+other
    
    #__radd__ = __add__
    
    

    def __sub__(self, other):
        if other.__class__ is NBcomplexe:
            x = self.a - other.a
            y = self.b - other.b
        else:
            
        #elif other.__class__ is float or other.__class__ is int: 
            x = self.a - other
            y = self.b
        return NBcomplexe(x,y)

        
    
    def __rsub__(self, other):
        """
        other - self
        
        self NBcomplexe
        
        ex : 2-(3+i)

        Parameters
        ----------
        self
        other

        Returns
        -------
        -(self-other)

        """
        return -(self-other)
        
        
        
    def __neg__(self):
        return NBcomplexe(-self.a, -self.b)

    def __mul__(self, other):
        if other.__class__ is NBcomplexe:
            x = self.a * other.a - self.b * other.b
            y = self.a * other.b + self.b * other.a
        else:
            x = self.a * other
            y = self.b * other
        return NBcomplexe(x,y)

        
        
        
        

    __rmul__ = __mul__
    
    def __truediv__(self, other):
        if other.a * other.a + other.b * other.b != 0:
            x = (self.a * other.a + self.b * other.b) / (other.a * other.a + other.b * other.b)
            y = (self.b * other.a - self.a * other.b) / (other.a * other.a + other.b * other.b)
            return NBcomplexe(x,y)
        else:
            return ZeroDivisionError
    
    def module(self):
        return  sqrt( self.a * self.a + self.b * self.b)

    def arg(self):
        if self.a != 0:
            return degrees(atan(self.b / self.a)) * pi/180
        else: 
            return ZeroDivisionError

    def conjuge(self):
        return NBcomplexe(self.a, -self.b)

    def affiche(self):#Implémenter plutôt l'affichage d'une LISTE de complexe : je n'ai pas compris ce que vous voulez 
        """
        Affiche Le nombre complex dans un graphique matplotlib tel que : x = la partie reel ; y = partie imaginaire
        """
        x = self.a
        y = self.b
        plt.plot(x,y, color='green', marker='+')
        plt.grid()
        plt.title(("Affichage de {}").format(str(NBcomplexe(self.a, self.b))))


# =============================================================================
z1=NBcomplexe(1,1)   #A intégrer dans les tests des fonctions
assert z1==z1
assert z1+z1==NBcomplexe(2,2)
assert z1*z1==NBcomplexe(0,2)
assert z1.conjuge()==NBcomplexe(1,-1)
assert z1.arg()==0.7853981633974483
assert z1.module()==1.4142135623730951
assert str(z1-z1)==f"0"


if __name__ == "__main__":
    import doctest
    doctest.testmod()#Pour tester les docString

    z1=NBcomplexe(1,1)
    z2=NBcomplexe(2,1)
    print(f"{z1} * {z2} = {z1*z2}")
    print(f"{z1} + {z2} = {z1+z2}")
    print(f"{z1} - {z2} = {z1-z2}")
    print(f"{z1} / {z2} = {z1/z2}")
    
    
    
    #z3=NBcomplexe( Fraction(1,2),1)
    
    #TypeError: unsupported operand type(s) for %: 'Fraction' and 'int'
    
    #z4=NBcomplexe( 1,Fraction(1,3))
    #print(f"{z3} * {z4} = {z3*z4}")
    #print(f"{z3} + {z4} = {z3+z4}")
    #print(f"{z3} - {z4} = {z3-z4}")
    #print(f"{z3} / {z4} = {z3/z4}")








