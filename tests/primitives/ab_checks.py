"""Примитивы для проверки ab-параметров, сигнала и конвенции углов."""

import numpy as np
from mag_nav.signal.ab_params import ab_from_amplitude_phase, amplitude_phase_from_ab
from mag_nav.signal.recovery import signal_from_ab
from mag_nav.convention import euler_to_rotation

def is_roundtrip_ok(A, phi):
    """
    Проверяет roundtrip конвертацию:
    (A, phi) -> (a, b) -> (A2, phi2).
    Должно выполняться A == A2 и (phi == phi2) (с учетом периода 2pi, хотя для phi в [-pi, pi]
    при A>0 это точное совпадение).
    """
    a, b = ab_from_amplitude_phase(A, phi)
    A2, phi2 = amplitude_phase_from_ab(a, b)
    return np.allclose(A, A2, atol=1e-10) and np.allclose(phi, phi2, atol=1e-10)

def is_signal_ok(a, b, omega, t, expected):
    """
    Проверяет что signal_from_ab выдает ожидаемые значения.
    """
    signal = signal_from_ab(a, b, omega, t)
    return np.allclose(signal, expected, atol=1e-10)

def is_convention_ok(alpha, beta, gamma, expected_matrix):
    """
    Проверяет что euler_to_rotation возвращает матрицу, близкую к ожидаемой.
    """
    rot = euler_to_rotation(alpha, beta, gamma)
    return np.allclose(rot.as_matrix(), expected_matrix, atol=1e-10)
