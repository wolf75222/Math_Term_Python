#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
email: romaindespoul@gmail.com
github: https://github.com/wolf75222/Math_Term_Python/blob/main/suite.py
"""

# =============================================================================
import inspect
import matplotlib.pyplot as plt
# =============================================================================


class Suite(object):

    def __init__(self, nom="u"):
        """
        -------
        Une classe abstraite de Suite
        """
        self.nom = nom

    def __call__(self):
        """
        -------
        """
        raise NotImplementedError

    def __str__(self):
        """
        -------
        """
        raise NotImplementedError

    def afficheGraphique(self):
        """
        -------
        Affiche un graphique des 100 premiers termes de la suite
        """
        lm = [m for m in range(100)]
        lc = [self(m) for m in lm]
        plt.plot(lm, lc, ".")
        plt.title(f"{self.nom}")
        plt.show()

    def rang(self, val, nMax=10000):
        """
        -------
        le rang où on trouve val
        """
        n = 0
        while self(n) != val:
            n += 1
            if n > nMax:
                return -1
        return n


class SuiteRec(Suite):

    def __init__(self, nom, val0=2, f=lambda x: x+2):
        """
        -------
        Une classe de Suite récurrente
        * Un+1 = f(Un) : suite définie par récurrence
        (on donne la fonction f et le premier terme)
        """
        super().__init__(nom)
        self.f = f
        self.dVal = dict()
        self.dVal[0] = val0

    def __call__(self, n):
        """
        a>>> u(2)
        7

        -------
        La valeur de la suite en n
        """
        res = self.dVal[0]
        if n in self.dVal.keys():
            res = self.dVal[n]
            print(res)
            print(self.dVal)
            return res
        else:
            for i in range(n):
                res = self.f(res)
                self.dVal[i] = res
                print(res)
                print(self.dVal)
                return res

    def rang(self, val, nMax):
        """
        -------
        """
        pass

    def __repr__(self):
        """
        >>> u
        SuiteRec("u", 1, lambda x: x+3)

        -------
        retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.
        """
        return str(inspect.getsourcelines(self.f)[0]).strip("['\\n']").split(" = ")[1]

    def __str__(self):
        """
        -------
        """
        pass


class SuiteFn(Suite):

    def __init__(self, nom, f=lambda n: n+3):
        """
        -------
        Une classe de suite tel que:
        * Un= f(n) : suite définie par son terme général
        (on donne la fonction f)
        """
        super().__init__(nom)
        self.f = f

    def __call__(self, n):
        """
        -------
        La valeur de la suite en n
        """
        pass

    def rang(self, val, nMax):
        """
        -------
        """
        pass

    def __repr__(self):
        """
        -------
        retourne une représentation sous forme de chaîne de caractères imprimable de l'objet passé.
        """
        return str(inspect.getsourcelines(self.f)[0]).strip("['\\n']").split(" = ")[1]

    def __str__(self):
        """
        -------
        """
        pass


if __name__ == "__main__":
    u = SuiteRec("u", 1, lambda x: x+3)
    import doctest
    doctest.testmod()
    u(2)
    u(2)
