# mag_nav/convention.py
"""Единственное место, где зафиксированы конвенции проекта."""

from scipy.spatial.transform import Rotation

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


# Система координат: правосторонняя, X-вперёд, Y-влево, Z-вверх (если не оговорено иное)
# Единицы: метры, Тесла, радианы
