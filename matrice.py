#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# =============================================================================
# Romain.D 19/12/2021
# =============================================================================

from math import sqrt, degrees, atan, pi
import numpy as np
import matplotlib as plt
from mpl_toolkits import mplot3d


class Matrice:
    """
        La class Matrice tel que:

        Une matrice A de dimension n × p à termes dans R est un
        tableau de réels de n lignes et p colonnes

        soit : A = (aij)

        ij est le coefficient de A situé à l’intersection de la ligne i et de la colonne j.
        Mn,p(R) est l’ensemble des matrice de dimension n × p.
    """

    def __init__(self, lst):
        """
        Class Matrice :
            Une matrice A de dimension n × p à termes dans R est un
            tableau de réels de n lignes et p colonnes.

        Parameters
        ----------
        lst : TYPE list imbriqué
            Le tableau qui défini la matrice.

        Returns
        -------
        None.

        """
        self.tableau = lst
        self.lignes = len(lst)
        self.colonnes = len(lst[0])

    def matriceDeZero(l, c):
        """
        Parameters
        ----------
        l : floor ou int
            lignes
        c : floor ou int
            colonnes

        Returns
        -------
        Matrice
            Renvoie une Matrice de zero tel que : M(l,c), par exemple M0=[[0,0,0],[0,0,0]]
        """

        lst = [[0 for k in range(c)] for i in range(l)]
        return Matrice(lst)

    def identite(n):
        """
        Parameters
        ----------
        n : init
            Ordre de la matrice I

        Returns
        -------
        I : Matrice
                La matrice identité ou unité d’ordre n, notée In, est la matrice carrée d’ordre n
        qui possède des "1" sur sa diagonale principale et des "0" ailleurs.


        """
        I = Matrice.matriceDeZero(n, n)
        for i in range(n):
            I.tableau[i][i] = 1
        return I

    def __str__(self):
        """
        Returns
        -------
        st : String
            str() retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.

        """
        st = "\n-----\n"
        m = 0
        for i in self:
            s = str(i)
            m = max(m, len(s))
        for ligne in self.tableau:
            for i in ligne:
                s = str(i)
                esp = " " * (m - len(s))
                st += esp + s + " "
            st += "\n"
        st += "-----\n"
        return st

    def __repr__(self):
        """
        Returns
        -------
        s : String
            repr() retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.

        """
        return f"Matrice({self.lignes}, {self.colonnes}, {self.tableau})"

    def __getitem__(self, idx):
        """
        Définit le comportement de l'utilisation des crochets [] sur les instances
        de cette classe.

        __getitem__est utilisé pour implémenter des appels comme self[key]
        https://qastack.fr/programming/43627405/understanding-getitem-method

        accès aux éléments en lecture	objet[key]	__getitem__(self,key)

        Parameters
        ----------
        idx : init
            index
        Returns
        -------
           par exemple m[0]

        """
        return self.tableau[idx]

    def __setitem__(self, idx, lst):
        """
        Pour définir la valeur

        Parameters
        ----------
        idx : init
            index
        lst : list
            nouvelle liste

        Returns
        -------
            par exemple m[2]=[3,3,3,3]

        """
        self.tableau[idx] = lst

    def __add__(self, other):
        """
        Soit A = (aij) et B = (bij) de même dimension et k un réel.
        • L’addition A + B est la matrice C = (cij) telle que cij = aij + bij

        Parameters
        ----------
        other : TYPE Matrice
            La matrice à additionner.

        Returns
        -------
        self + other

        """
        if self.lignes != other.lignes or self.colonnes != other.colonnes:
            raise(
                ValueError, "Pour additionner deux matrices, la taille des matrices doit être la même.")

        m = Matrice.matriceDeZero(self.lignes, self.colonnes)
        for i in range(self.lignes):
            for j in range(self.colonnes):
                m[i][j] = self[i][j] + other[i][j]

        return m

    def __sub__(self, other):
        """
        Soit A = (aij) et B = (bij) de même dimension et k un réel.
        • La soustraction A - B est la matrice C = (cij) telle que cij = aij - bij

        Parameters
        ----------
        other : TYPE Matrice
            La matrice à soustraire.

        Returns
        -------
        self + other

        """
        if self.lignes != other.lignes or self.colonnes != other.colonnes:
            raise(
                ValueError, "Pour soustraire deux matrices, la taille des matrices doit être la même.")

        m = Matrice.matriceDeZero(self.lignes, self.colonnes)
        for i in range(self.lignes):
            for j in range(self.colonnes):
                m[i][j] = self[i][j] - other[i][j]
        return m

    def __mul__(self, other):
        """
        Soit A = (aij) de dim. n×p et B = (bij) de dim. p×q.
        Le produit AB est la matrice C = (cij) de dim. n×q telle que : cij = somme de p a k=1 aik bkj

        Returns
        -------
        m : Matrice
            le Produit de deux matrices

        """
        if self.colonnes != other.lignes:
            raise(ValueError, "Le nombre de colonnes doit être égal")
        m = Matrice.matriceDeZero(self.lignes, other.colonnes)
        for i in range(m.lignes):
            for j in range(m.colonnes):
                m[i][j] = sum(self[i][k]*other[k][j]
                              for k in range(self.colonnes))
        return m

    def __eq__(self, other):
        """
        Parameters
        ----------
        other : Matrice
            La Matrice a comparer

        Returns
        -------
        bool
            Renvoie true si les Matrice sont égales

        """
        return self.tableau == other.tableau

    def estUneMatriceCarre(self):
        """
        Returns
        -------
        bool
            Renvoie True si la matrice est carre

        """
        return self.lignes == self.colonnes

    def transposition(self):
        """
        La transposée d’une matrice A = (aij) de dimension n × p est
        la matrice, notée A
        T = (cij), de dimension p × n telle que cij = aji.

        Returns
        -------
        m : Matrice
            La Matrice Transposée

        """
        x = self.tableau
        m = Matrice.matriceDeZero(self.colonnes, self.lignes)
        for i in range(len(x)):
            for j in range(len(x[0])):
                m[j][i] = x[i][j]
        return m

    def __neg__(self):
        """
        Renvoie l'opposé de la Matrice

        Returns
        -------
        Matrice
            opposé de la matrice

        """

        for i in range(self.lignes):
            for j in range(self.colonnes):
                self[i][j] *= -1

        return self

    def __ne__(self, other):
        """
        non égal	 != ou <>	__ne__(self,other)

        Parameters
        ----------
        other : Matrice
           La deuxieme matrice a comparer

        Returns
        -------
        bool
            True si les matrice sont différentes

        """
        if self == other:
            return False
        else:
            return True

    def __call__(self, i, j):
        """
        Matrice(3, 3, [[-2, 4, 9], [-34, -31, -39], [1, 19, 18]])
        M1(1,0)
        -34

        Parameters
        ----------
        i : int
            lignes
        j : int
            colonnes

        Returns
        -------
        int
            Si l’objet est appelée comme une fonction, il retournera la valeur retournée par cette méthode.

        """
        return self.tableau[i][j]

    def __iter__(self):
        """
        Pour faire des boucles comme for i in I, en parcourant les valeurs de i
        https://qastack.fr/programming/4019971/how-to-implement-iter-self-for-a-container-object-python

        Yields
        ------
        i : int
            yield
         renvoie une valeur, mais ne sort pas de la fonction. yield fabrique un objet generateur qui par exemple est utilisé dans la                      boucle fors

        """

        for ligne in self.tableau:
            for i in ligne:
                yield i

    def inverse(self):
        """
        Une matrice carrée A d’ordre n est inversible si, et seulement
        si, il existe une matrice carrée d’ordre n, appelée matrice inverse A−1, telle que :
            AA−1 = A−1A = In
        Si A−1 n’existe pas, on dit que la matrice M est singulière

        Returns
        -------
        None.

        """
        pass


M0 = Matrice.matriceDeZero(3, 3)

MI = Matrice.identite(3)

M1 = Matrice([
    [-2,   4,   9],
    [-34, -31, -39],
    [1,  19,  18]])

M2 = Matrice.identite(3) + Matrice.identite(3)

M3 = M2 * M2

M4 = Matrice([[1, 2],
              [3, 4],
              [5, 6]])

M5 = Matrice.identite(4)
#Matrice(4, 4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
M5[2] = [4, 4, 4, 4]
#Matrice(4, 4, [[1, 0, 0, 0], [0, 1, 0, 0], [4, 4, 4, 4], [0, 0, 0, 1]])


assert MI.estUneMatriceCarre() == True
assert M4.transposition() == Matrice([[1, 3, 5],
                                      [2, 4, 6]])

assert -M4 == Matrice([[-1, -2],
                       [-3, -4],
                       [-5, -6]])

assert Matrice.identite(3) != M4

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    M10 = Matrice([
        [9,   6,   7],
        [-34, 100, 40],
        [-1,  134,  28]])

    M11 = Matrice([
        [1,   0,   0],
        [-9, -167, 89],
        [4,  55,  78]])

    print(f"{M10} + {M11} = {M10+M11}")
    print(f"{M10} - {M11} = {M10-M11}")
    print(f"{M10} * {M11} = {M10*M11}")
    #print(f"{M10} / {M11} = {M10/M11}")
    #print(f"{2} * {M10} = {2*M10}")
    #print(f"{M10} * {2} = {M10*2}")
    #print(f"{2} + {M10} = {2+M10}")
    #print(f"{M10} + {2} = {M10+2}")
