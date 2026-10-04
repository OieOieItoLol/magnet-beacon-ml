# mag_nav/convention.py
"""Единственное место, где зафиксированы конвенции проекта."""

from scipy.spatial.transform import Rotation
import math

# Порядок углов Эйлера: ZYX (внешний → внутренний)
# R = Rz(gamma) @ Ry(beta) @ Rx(alpha)
EULER_SEQ = "ZYX"


def euler_to_rotation(alpha: float, beta: float, gamma: float) -> Rotation:
    """Единственная функция перевода углов в Rotation."""
    return Rotation.from_euler(EULER_SEQ.lower(), [gamma, beta, alpha])


def rotation_to_euler(rot: Rotation) -> tuple[float, float, float]:
    """Единственная функция обратного перевода. Возвращает (alpha, beta, gamma)."""
    angles = rot.as_euler(EULER_SEQ.lower())
    return angles[2], angles[1], angles[0]  # gamma, beta, alpha → alpha, beta, gamma

def roundtrip_euler(alpha: float, beta: float, gamma: float) -> bool:
    """
    Проверяет roundtrip конвертацию углов через Rotation.
    Возвращает True если углы совпали с точностью 1e-10.
    """
    rot = euler_to_rotation(alpha, beta, gamma)
    a, b, g = rotation_to_euler(rot)
    return (
        math.isclose(alpha, a, abs_tol=1e-10) and
        math.isclose(beta, b, abs_tol=1e-10) and
        math.isclose(gamma, g, abs_tol=1e-10)
    )

# Система координат: правосторонняя, X-вперёд, Y-влево, Z-вверх (если не оговорено иное)
# Единицы: метры, Тесла, радианы
