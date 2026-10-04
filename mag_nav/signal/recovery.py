"""Восстановление мгновенного сигнала из a, b параметров."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def signal_from_ab(
    a: NDArray[np.float64],
    b: NDArray[np.float64],
    omega: float,
    t: NDArray[np.float64],
) -> NDArray[np.float64]:
    """s_i(t) = a_i·cos(ωt) + b_i·sin(ωt) для каждого компонента и момента времени.

    Args:
        a: (N,) — a-параметры
        b: (N,) — b-параметры
        omega: угловая частота, рад/с
        t: (M,) — моменты времени

    Returns:
        (N, M) — сигнал для каждого компонента в каждый момент

    pre: len(a) == len(b)
    pre: omega > 0.0
    post: __return__.shape == (len(a), len(t))
    post: np.allclose(
        __return__[:, 0],
        a * np.cos(omega * t[0]) + b * np.sin(omega * t[0]),
        atol=1e-12
    )
    """
    wt = omega * t
    return a[:, None] * np.cos(wt)[None, :] + b[:, None] * np.sin(wt)[None, :]
