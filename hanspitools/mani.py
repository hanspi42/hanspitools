# -*- coding: utf-8 -*-
"""
Hanspeter Schmid, FHNW/ISE
This file contains tricks to manipulate symbolic expressions.
"""

import sympy as sp
import numpy as np

def nicepoly(p,x):
    """

    Parameters
    ----------
    p : SymPy expression
        a polynomial in any variable, e.g., s
    x : SymPy symbol
        the variable, e.g., s

    Returns
    -------
    This function takes a sympy function p, tries to interpret it as
    a polynomial in x, and re-writes it by using .factor() on all
    polynomial coefficients.  This can result in well interpretable
    expressions.

    """
    
    c = p.as_poly(x).all_coeffs()[::-1]
    return sum( [ x**i*(y.factor()) for y,i in zip(c,np.arange(np.size(c))) ] )

def numden(f,expression):
    """

    Parameters
    ----------
    f : lambda function with one variable
        A SymPy functon with one variable
    expression : SymPy expression
        The expression to modify

    Returns
    -------
    This function applies f() to the numerator and denominator of expression.

    """
    [n,d] = sp.fraction(expression)
    return f(n)/f(d)
    