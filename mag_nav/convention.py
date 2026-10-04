"""Единая точка фиксации конвенций проекта.

Все модули импортируют перевод углов ТОЛЬКО отсюда.
Никто не вызывает Rotation.from_euler напрямую вне этого файла.
"""

from __future__ import annotations

from scipy.spatial.transform import Rotation
import math

# Конвенция: R = Rz(gamma) @ Ry(beta) @ Rx(alpha)
# Это intrinsic 'zyx' в терминах scipy.
# Углы в радианах. Порядок аргументов всегда: (alpha, beta, gamma).
EULER_SEQ: str = "zyx"


def euler_to_rotation(alpha: float, beta: float, gamma: float) -> Rotation:
    """Перевод углов Эйлера (α, β, γ) в объект Rotation.

    pre: True  # углы любые, периодичность обрабатывает scipy
    post: isinstance(__return__, Rotation)
    """
    ...


def rotation_to_euler(rot: Rotation) -> tuple[float, float, float]:
    """Перевод Rotation обратно в (α, β, γ).

    pre: isinstance(rot, Rotation)
    post: len(__return__) == 3
    post: abs(__return__[0]) <= 3.14159265358979 + 1e-9  # alpha in [-π, π]
    """
    ...

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

def roundtrip_euler(alpha: float, beta: float, gamma: float) -> bool:
    """Проверка: euler → Rotation → euler ≈ identity (для использования в тестах).

    Не часть публичного API; вспомогательная функция для контрактов.
    """
    ...
