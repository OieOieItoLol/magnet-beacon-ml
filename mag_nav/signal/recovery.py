"""Восстановление сигнала из (a, b)."""

import numpy as np

def signal_from_ab(a, b, omega, t):
    """
    Восстанавливает сигнал.
    a: array-like, shape (N,)
    b: array-like, shape (N,)
    omega: float
    t: array-like, shape (M,)
    Возвращает ndarray shape (N, M).
    """
    a = np.asarray(a)
    b = np.asarray(b)
    t = np.asarray(t)
    return a[:, None] * np.cos(omega * t)[None, :] + b[:, None] * np.sin(omega * t)[None, :]
