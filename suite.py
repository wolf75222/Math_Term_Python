#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# {}
# []
# =============================================================================

# =============================================================================
import inspect
import matplotlib.pyplot as plt
# =============================================================================


class Suite(object):

    def __init__(self, val0=2, f=lambda x: x+2):
        """
        Une classe abstraite de Suite

        Parameters
        ----------
        val0 : float
            La valeur en 0. The default is 2.
        f : function
            La focntion qui renvoie l'image de x tel que Un+1=f(Un) The default is lambda(x: x+2).

        Returns
        -------
        None.

        """
        self.val0 = val0
        self.f = f

    def __call__(self, n):
        """
        Parameters
        ----------
        n : int
            le rang

        Returns
        -------
        res : float
            la valeur de la suite en n

        """
        res = self.val0
        for k in range(n):
            res = self.f(res)
        return res

    def construitGraphique(self):
        """
        -------
        Construit un graphique des 100 premiers termes de la suite

        """
        lm = [m for m in range(100)]
        lc = [self(m) for m in lm]
        plt.plot(lm, lc, ".")
        plt.title(f"{self}")

    def renvoieRang(self, val):
        """

        Parameters
        ----------
        val : float
            la valeur en n

        Returns
        -------
        n : int
            le rang ou on trouve val

        """
        n = 0
        while self(n) != val:
            n += 1
        return n

    def __repr__(self):
        """
        Returns
        -------
        s : String
            repr() retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.
        """
        return str(inspect.getsourcelines(self.f)[0]).strip("['\\n']").split(" = ")[1]

    def __str__(self):
        """
        Returns
        -------
            str() retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.
        """
        return f"Val0 = {self.val0} f = {self.f}"

    def __eq__(self, other):
        return self.val0 == other.val0 and self.f == other.f

    def __add__(self, other):
        if self.val0 < other.val0:
            x = self.val0
        else:
            x = other.val0
        y = self.f + other.f
        return Suite(x, y)


# =============================================================================
# Test __call__
u = Suite(1, lambda x: x+3)
assert u(2) == 7
# Test __repr__
# assert u == "Suite(1, lambda x: x+3)" ??


# =============================================================================
