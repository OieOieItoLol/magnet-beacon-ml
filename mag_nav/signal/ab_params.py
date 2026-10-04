"""a, b параметры сигнала и их связь с амплитудой/фазой.

Модель сигнала:  s_i(t) = a_i · cos(ωt) + b_i · sin(ωt)
Связь:           a = A·cos(φ),  b = −A·sin(φ)
Обратная:        A = √(a²+b²),  φ = atan2(−b, a)
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def ab_from_amplitude_phase(
    A: NDArray[np.float64],
    phi: NDArray[np.float64],
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """(A, φ) → (a, b) покомпонентно.

    pre: len(A) == len(phi)
    pre: all(A >= 0.0)  # амплитуда неотрицательна
    post: len(__return__[0]) == len(A)
    post: len(__return__[1]) == len(A)
    post: np.allclose(__return__[0]**2 + __return__[1]**2, A**2)
    """
    a = A * np.cos(phi)
    b = -A * np.sin(phi)
    return a, b


def amplitude_phase_from_ab(
    a: NDArray[np.float64],
    b: NDArray[np.float64],
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """(a, b) → (A, φ) покомпонентно.

    pre: len(a) == len(b)
    post: len(__return__[0]) == len(a)
    post: np.all(__return__[0] >= 0.0)  # A ≥ 0
    post: np.allclose(
        __return__[0] * np.cos(__return__[1]), a, atol=1e-12
    )
    post: np.allclose(
        -__return__[0] * np.sin(__return__[1]), b, atol=1e-12
    )
    """
    A = np.sqrt(a**2 + b**2)
    phi = np.arctan2(-b, a)
    return A, phi


def ab_roundtrip_check(
    A: NDArray[np.float64],
    phi: NDArray[np.float64],
) -> bool:
    """Вспомогательная: (A,φ) → (a,b) → (A',φ') ≈ (A,φ).

    Не часть публичного API.
    """
    a, b = ab_from_amplitude_phase(A, phi)
    A_prime, phi_prime = amplitude_phase_from_ab(a, b)
    if not np.allclose(A_prime, A, atol=1e-12):
        return False
    # Check phases while considering 2pi wrap-around
    phase_diff = np.angle(np.exp(1j * (phi_prime - phi)))
    return bool(np.allclose(phase_diff, 0.0, atol=1e-10))
