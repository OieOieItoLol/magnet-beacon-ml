import numpy as np
import math
from tests.primitives.ab_checks import is_roundtrip_ok, is_signal_ok, is_convention_ok
from mag_nav.convention import roundtrip_euler

def test_roundtrip():
    # случайные A>=0, phi в [-pi, pi], длина 3
    A = np.array([1.5, 0.0, 3.14])
    phi = np.array([-np.pi, 0.0, np.pi/2])
    assert is_roundtrip_ok(A, phi)

def test_signal():
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    omega = 2 * np.pi
    t = np.array([0, 0.25, 0.5])
    # a[:, None]*cos(omega*t)[None, :] + b[:, None]*sin(omega*t)[None, :]
    # omega*t = [0, pi/2, pi]
    # cos(omega*t) = [1, 0, -1]
    # sin(omega*t) = [0, 1, 0]

    # expected for i=0: a=1, b=0 -> 1*cos(ot) + 0*sin(ot) = [1, 0, -1]
    # expected for i=1: a=0, b=1 -> 0*cos(ot) + 1*sin(ot) = [0, 1, 0]
    # expected for i=2: a=0, b=0 -> 0*cos(ot) + 0*sin(ot) = [0, 0, 0]
    expected = np.array([
        [1, 0, -1],
        [0, 1, 0],
        [0, 0, 0]
    ], dtype=float)

    assert is_signal_ok(a, b, omega, t, expected)

def test_convention():
    alpha = 0
    beta = 0
    gamma = np.pi / 2
    # Поворот на 90 градусов вокруг Z
    # Rz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    expected_matrix = np.array([
        [0, -1, 0],
        [1,  0, 0],
        [0,  0, 1]
    ], dtype=float)
    assert is_convention_ok(alpha, beta, gamma, expected_matrix)

    # также проверяем roundtrip_euler
    assert roundtrip_euler(alpha, beta, gamma)
