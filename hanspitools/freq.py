# -*- coding: utf-8 -*-
"""
Hanspeter Schmid, FHNW/ISE
This file contains scripts useful in frequency analysis.
"""

import sympy as sp
import numpy as np

def amplitude(T,s,wn,target):
    """

    Parameters
    ----------
    T : SymPy function
        symbolic transfer function (e.g., Laplace varable s)
    s : SymPy symbol
        the symbol of the Laplace variable (e.g., s)
    wn : NumPy array
        contains the angular frequencies at which T will be evaluated
    target : list of tuples
        each tuple contains a SymPy symbol name and the numerical value
        that needs to be substituted for it.

    Returns
    -------
    A NumPy array of the absolute values of the Fourier transfer function
    that is obtained by substituting sy.I*omega for s, substituing all
    values from target into the function, and then evaluate it for all wn.

    """
    omega = sp.symbols('omega')
    Ta = T.subs(s,sp.I*omega).subs(target)
    Tl = sp.lambdify(omega, Ta, modules=['numpy'])
    return( np.abs(Tl(wn.astype('float'))) )

def phase(T,s,wn,target):
    """

    Parameters
    ----------
    T : SymPy function
        symbolic transfer function (e.g., Laplace varable s)
    s : SymPy symbol
        the symbol of the Laplace variable (e.g., s)
    wn : NumPy array
        contains the angular frequencies at which T will be evaluated
    target : list of tuples
        each tuple contains a SymPy symbol name and the numerical value
        that needs to be substituted for it.

    Returns
    -------
    A NumPy array of the phase values of the Fourier transfer function
    that is obtained by substituting sy.I*omega for s, substituing all
    values from target into the function, and then evaluate it for all wn.
    
    The phase is unwrapped and given in degrees.

    """
    omega = sp.symbols('omega')
    Ta = T.subs(s,sp.I*omega).subs(target)
    Tl = sp.lambdify(omega, Ta, modules=['numpy'])
    return( np.unwrap(np.angle(Tl(wn.astype('float'))))*180/np.pi )