import numpy as np
import math
from tests.primitives.ab_checks import check_roundtrip_ab, check_signal_value
from mag_nav.convention import roundtrip_euler, euler_to_rotation
from mag_nav.signal.ab_params import ab_from_amplitude_phase, amplitude_phase_from_ab
from mag_nav.signal.recovery import signal_from_ab

def test_roundtrip():
    # случайные A>=0, phi в [-pi, pi], длина 3
    A = np.array([1.5, 0.0, 3.14])
    phi = np.array([-np.pi, 0.0, np.pi/2])

    a, b = ab_from_amplitude_phase(A, phi)
    A_back, phi_back = amplitude_phase_from_ab(a, b)

    assert check_roundtrip_ab(A, phi, a, b, A_back, phi_back)

def test_signal():
    a = np.array([1, 0, 0], dtype=float)
    b = np.array([0, 1, 0], dtype=float)
    omega = 2 * np.pi
    t = np.array([0, 0.25, 0.5], dtype=float)

    expected = np.array([
        [1, 0, -1],
        [0, 1, 0],
        [0, 0, 0]
    ], dtype=float)

    # Also check using check_signal_value primitve for each timepoint
    for j, tj in enumerate(t):
        assert check_signal_value(a, b, omega, tj, expected[:, j])

def test_convention():
    alpha = 0.0
    beta = 0.0
    gamma = np.pi / 2
    # Поворот на 90 градусов вокруг Z
    # Rz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    expected_matrix = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ], dtype=float)

    rot = euler_to_rotation(alpha, beta, gamma)
    assert np.allclose(rot.as_matrix(), expected_matrix, atol=1e-12)

    # также проверяем roundtrip_euler
    assert roundtrip_euler(alpha, beta, gamma)
