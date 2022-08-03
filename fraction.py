#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 00:06:59 2021

@author: romain Despoullains
"""

from math import sqrt, degrees, atan, pi
import numpy as np
import matplotlib as plt
from mpl_toolkits import mplot3d

def estNbPremiers(n):
    """
    Un nombre premier est un entier naturel qui admet exactement
    deux diviseurs : 1 et lui-même
    Tout entier naturel n tel que n > 2 admet un diviseur premier.
    Si n n’est pas premier, alors il admet un diviseur premier p tel que : 2 <= p <= sqrt(n)

    Renvoie si n est premier ou non
    """
    i=2
    if n%i==0:
        return False
    i+=1
    while i**2<=n: ## A éviter puisque que tu calucles un carré à chaque itération
        # Comment éviter ?
        if n%i==0:
            return False
        i+=2
    return True

def nbPremierSuivant(n):
    """
    Renvoie le nb premier suivant a n

    n = 18
    on regarde si n+1(19) estnbpremier
        si oui on le renvoie
    sinon:
        n+=1(20)

    """
    while estNbPremiers(n)==False:
        n+=1  #Tu touches au paramètre : je n'aime pas
    return n

# =============================================================================

assert estNbPremiers(13)
assert not(estNbPremiers(14))
assert nbPremierSuivant(18)==19

# =============================================================================
# =============================================================================


def PGCD(a,b):
    """
    Renvoie le PGCD des entiers a et b
    gcd retourne le plus grand commun diviseur de (x,y)
    """
    #assert a>0 and b>0
    if (a or b)<0:
        a=abs(a)
        b=abs(b)
    while b!=0:
        a, b = b, a%b
    return a

# =============================================================================
assert PGCD(60,36)==12
assert PGCD(35,22)==1
# =============================================================================

class Fraction():
    """
    La class des Fractions""
        numérateur  ENTIER RELATIF
        dénominateur ENTIER NATUREL non NUL
    """
    def __init__(self, numerateur:int, denominateur:int=1):
        if denominateur==0:                  #assert plutôt
            raise ZeroDivisionError
        #assert numerateur>0 and denominateur >0
        d=PGCD(numerateur,denominateur)
        self.numerateur = numerateur/d   #Nèutilise QUE la division entièr : avec le // ?
        self.denominateur = denominateur/d  #Oui mais ça passe car d divise toujours les num et den
        #Il faudra gérer les signes Fraction(4,-3) doit renvoyer Fraction(-4,3)


    def tuplesSimplifie(self, x, y):
        """Retourne le tuples simplifier par le meme facteur"""
        facteur = PGCD(x, y)
        a = x / facteur  
        b = y/ facteur
        return a, b

    def fractionDepuisObjet(self, objet):
        """Convertir un init en Fraction"""
        if isinstance(objet, (int)): #On en reparlera sous peu !!!!!!!! :  et donc ? #il faut qu'on en parle écris un exemple d'utilisation et pense d'avantage à utiliser le constructeur
            return Fraction(objet)#il y a d'autre objets mathématiques à mettre en fraction
        else:
            raise NotImplementedError

    def __str__(self):
        if self.denominateur == 1:
            return f"{int(self.numerateur)}"
        else:
            return  f"{int(self.numerateur)} / {int(self.denominateur)}"
    def __repr__(self):  
        """
        >>> Fraction(6)
        Fraction(6,1)
        >>> Fraction(6,12)
        Fraction(1,2)
        """
        return  f"Fraction({int(self.numerateur)},{int(self.denominateur)})"

    def __mul__(self, other):
        """
        >>> Fraction(2,3)*(Fraction(-2,3)*3)
        Fraction(-4,3)
        """
        if type(other) is Fraction:
            num = self.numerateur * other.numerateur
            denom = self.denominateur * other.denominateur
            return Fraction(int(num), int(denom))
        elif type(other) is int:
            num = self.numerateur * other
            denom = self.denominateur
            return Fraction(int(num), int(denom))
        else:
            raise NotImplementedError

#    def __rmul__(self, other):
#        return self.__mul__(other)

    __rmul__ = __mul__


    def __eq__(self,other):
        """ Revoir true si les deux fractions sont égales"""
        if type(other) is Fraction:
            f1 = self.numerateur * other.denominateur
            f2 = other.numerateur * self.denominateur
            return f1 == f2
        elif type(other) is int:
            return int(round(self.numerateur/self.denominateur, 0)) == other
        else:
            raise NotImplementedError
#        if not isinstance(other, Fraction):
#            other = self.fractionDepuisObjet(other)
#        if type(other) is Fraction:
#            if self.numerateur == other.numerateur and self.denominateur == other.denominateur:
#                return True
#            else:
#                return False

    def __ne__(self,other):
        """ Revoir true si les deux fractions sont différentes"""
        # if type(other) is Fraction:#Tu n'utilises pas assez les fonctions déjà implémentée
        #     f1 = self.numerateur * other.denominateur
        #     f2 = other.numerateur * self.denominateur
        #     return f1 != f2
        # elif type(other) is int:
        #     return int(round(self.numerateur/self.denominateur, 0)) != other
        # else:
        #     raise NotImplementedError
        if self == other:
            return False
        else:
            return True
        

    def __lt__(self,other):
        """Renvoie True si 	self < other"""
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        return (self - other).numerateur < 0


    def __gt__(self, other):
        """Renvoie True si 	self > other"""
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        return (self - other).numerateur > 0

    def __le__(self, other):
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        return (self - other).numerateur <= 0

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        return (self - other).numerateur >= 0


    def __hash__(self):
        """https://www.pythontutorial.net/python-oop/python-__hash__/"""
        return hash(self.numerateur /self.denominateur)

    def float(self):
        return (self.numerateur /self.denominateur)

    def __div__(self, other):
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        num = self.numerateur * other.denominateur
        denom = self.denominateur * other.numerateur
        return Fraction(num, denom)

    
    __rdiv__ = __div__

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = self.fractionDepuisObjet(other)
        denom = self.denominateur * other.denominateur
        num = self.numerateur * other.denominateur + self.denominateur * other.numerateur
        return Fraction(num, denom)



    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            #other = self.fractionDepuisObjet(other)
            return Fraction(self.numerateur - other * self.denominateur, self.denominateur)#a/b - c = (a-cb)/b
        denom = self.denominateur * other.denominateur
        num = self.numerateur*other.denominateur - self.denominateur*other.numerateur
        return Fraction(num, denom)

    __rsub__ = __sub__
    
    
# =============================================================================

f12=Fraction(1,2)  
f13=Fraction(1,3)
res=(f12==f13)
f56=Fraction(5,6)
f56b=f12+f13
f16=Fraction(1,6)
# =============================================================================
assert f12>f13  #A faire : http://lptms.u-psud.fr/wiki-cours/index.php/Python:_Surcharge
assert f56==f56b
assert 5==(f56*6)
assert 5==(6*f56)

assert (f56-f12*f13)==2*f13

#Je voudrais aussi faire ça :
#z1=NBcomplexe(f12,f12)


#Tu pourras ensuite  faire une classe polynôme



if __name__ == "__main__":
    import doctest
    doctest.testmod()#Pour tester les docString

    f12=Fraction(1,2)
    f13=Fraction(1,3)
    print(f"{f12} + {f13} = {f12+f13}")
    print(f"{f12} - {f13} = {f12-f13}")
    print(f"{f12} * {f13} = {f12*f13}")
    #print(f"{f12} / {f13} = {f12/f13}")
    print(f"{2} * {f12} = {2*f12}")
    print(f"{f12} * {2} = {f12*2}")
    print(f"{2} + {f12} = {2+f12}")
    print(f"{f12} + {2} = {f12+2}")
    
    
    for k in range(0,5):
        n  = [1,3,7,9,13,15]
        for i in range(len(n)):
            N = n[i]+k
            if estNbPremiers(N):
                print("_____________")
                print(n[i])
                print(k)
                print("_____________")
