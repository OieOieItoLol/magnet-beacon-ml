"""Переход между параметрами (A, phi) и (a, b)."""

import numpy as np

def ab_from_amplitude_phase(A, phi):
    """
    Вычисляет (a, b) из (A, phi).

    a = A * cos(phi)
    b = -A * sin(phi)

    A: array-like
    phi: array-like
    Возвращает (a, b).
    """
    A = np.asarray(A)
    phi = np.asarray(phi)
    return A * np.cos(phi), -A * np.sin(phi)

def amplitude_phase_from_ab(a, b):
    """
    Вычисляет (A, phi) из (a, b).

    A = sqrt(a**2 + b**2)
    phi = arctan2(-b, a)
    A всегда >= 0

    a: array-like
    b: array-like
    Возвращает (A, phi).
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return np.sqrt(a**2 + b**2), np.arctan2(-b, a)
