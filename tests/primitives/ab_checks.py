"""Примитивы проверки ab-параметров. Чистые функции, без pytest."""

import numpy as np


def check_ab_magnitude(a: np.ndarray, b: np.ndarray, A_expected: np.ndarray) -> bool:
    """a² + b² == A² покомпонентно."""
    return bool(np.allclose(a**2 + b**2, A_expected**2, rtol=1e-12))


def check_ab_phase(a: np.ndarray, b: np.ndarray, phi_expected: np.ndarray) -> bool:
    """atan2(-b, a) == φ покомпонентно (с учётом периодичности)."""
    phi_recovered = np.arctan2(-b, a)
    diff = np.angle(np.exp(1j * (phi_recovered - phi_expected)))
    return bool(np.allclose(diff, 0.0, atol=1e-12))


def check_signal_value(
    a: np.ndarray,
    b: np.ndarray,
    omega: float,
    t: float,
    s_expected: np.ndarray,
) -> bool:
    """s(t) = a·cos(ωt) + b·sin(ωt) в одной точке."""
    s = a * np.cos(omega * t) + b * np.sin(omega * t)
    return bool(np.allclose(s, s_expected, atol=1e-12))


def check_roundtrip_ab(
    A: np.ndarray,
    phi: np.ndarray,
    a: np.ndarray,
    b: np.ndarray,
    A_back: np.ndarray,
    phi_back: np.ndarray,
) -> bool:
    """(A,φ)→(a,b)→(A',φ'): A'≈A, φ'≈φ."""
    if not np.allclose(A_back, A, atol=1e-12):
        return False
    phase_diff = np.angle(np.exp(1j * (phi_back - phi)))
    return bool(np.allclose(phase_diff, 0.0, atol=1e-10))
