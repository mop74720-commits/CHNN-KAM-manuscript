"""Minimal verification suite for the CHNN--KAM full Chinese draft.

This file intentionally covers only the analytic V1--V3 tests.  It is not a
replacement for the archived prototype or for the future COMSOL data pipeline.
All variables are dimensionless unless explicitly stated otherwise.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


Array = np.ndarray
Force = Callable[[float], float]


@dataclass(frozen=True)
class Oscillator:
    mass: float = 1.0
    stiffness: float = 2.0
    damping_rate: float = 0.0

    def validate(self) -> None:
        if self.mass <= 0.0 or self.stiffness <= 0.0:
            raise ValueError("mass and stiffness must be positive")
        if self.damping_rate < 0.0:
            raise ValueError("damping_rate must be nonnegative")


def energy(z: Array, model: Oscillator) -> float:
    q, p = np.asarray(z, dtype=float)
    return 0.5 * p * p / model.mass + 0.5 * model.stiffness * q * q


def exact_conservative(t: float, z0: Array, model: Oscillator) -> Array:
    if model.damping_rate != 0.0:
        raise ValueError("exact_conservative requires zero damping")
    q0, p0 = np.asarray(z0, dtype=float)
    omega = np.sqrt(model.stiffness / model.mass)
    q = q0 * np.cos(omega * t) + p0 * np.sin(omega * t) / (model.mass * omega)
    p = p0 * np.cos(omega * t) - model.mass * omega * q0 * np.sin(omega * t)
    return np.array([q, p])


def midpoint_step(
    z: Array,
    t: float,
    h: float,
    model: Oscillator,
    force: Force = lambda _t: 0.0,
) -> Array:
    """Closed implicit-midpoint step for qdot=p/m, pdot=-kq-gamma*p+f."""
    model.validate()
    q, p = np.asarray(z, dtype=float)
    m = model.mass
    k = model.stiffness
    gamma = model.damping_rate
    f_mid = float(force(t + 0.5 * h))
    eps_h = k * h * h / (4.0 * m) + gamma * h / 2.0
    p_new = ((1.0 - eps_h) * p - k * h * q + h * f_mid) / (1.0 + eps_h)
    q_new = q + h * (p_new + p) / (2.0 * m)
    return np.array([q_new, p_new])


def damping_half_step(z: Array, h_half: float, model: Oscillator) -> Array:
    q, p = np.asarray(z, dtype=float)
    return np.array([q, np.exp(-model.damping_rate * h_half) * p])


def conservative_midpoint_step(z: Array, t: float, h: float, model: Oscillator) -> Array:
    conservative = Oscillator(model.mass, model.stiffness, 0.0)
    return midpoint_step(z, t, h, conservative)


def conformal_strang_step(z: Array, t: float, h: float, model: Oscillator) -> Array:
    """D(h/2) o H(h) o D(h/2); exact conformal factor exp(-gamma*h)."""
    z1 = damping_half_step(z, 0.5 * h, model)
    z2 = conservative_midpoint_step(z1, t, h, model)
    return damping_half_step(z2, 0.5 * h, model)


def integrate(
    step: Callable[[Array, float, float, Oscillator], Array],
    z0: Array,
    h: float,
    steps: int,
    model: Oscillator,
) -> Array:
    trajectory = np.empty((steps + 1, 2), dtype=float)
    trajectory[0] = np.asarray(z0, dtype=float)
    for index in range(steps):
        trajectory[index + 1] = step(trajectory[index], index * h, h, model)
    return trajectory


def finite_difference_jacobian(
    step: Callable[[Array, float, float, Oscillator], Array],
    z: Array,
    t: float,
    h: float,
    model: Oscillator,
    eps: float = 1.0e-7,
) -> Array:
    z = np.asarray(z, dtype=float)
    base = step(z, t, h, model)
    jacobian = np.empty((2, 2), dtype=float)
    for column in range(2):
        shifted = z.copy()
        shifted[column] += eps
        jacobian[:, column] = (step(shifted, t, h, model) - base) / eps
    return jacobian


def structure_defect(jacobian: Array, factor: float) -> float:
    j_matrix = np.array([[0.0, 1.0], [-1.0, 0.0]])
    residual = jacobian.T @ j_matrix @ jacobian - factor * j_matrix
    return float(np.linalg.norm(residual, ord="fro"))


def complex_round_trip(z: Array) -> float:
    q, p = np.asarray(z, dtype=float)
    zeta = (q + 1j * p) / np.sqrt(2.0)
    recovered = np.array(
        [(zeta + np.conjugate(zeta)).real / np.sqrt(2.0),
         (-1j * (zeta - np.conjugate(zeta))).real / np.sqrt(2.0)]
    )
    return float(np.linalg.norm(recovered - np.asarray(z, dtype=float)))


def conservative_order_test() -> dict[str, float]:
    model = Oscillator(mass=1.0, stiffness=2.0, damping_rate=0.0)
    z0 = np.array([1.0, 0.3])
    final_time = 2.0
    step_sizes = np.array([0.2, 0.1, 0.05, 0.025])
    errors = []
    energy_drifts = []
    for h in step_sizes:
        steps = int(round(final_time / h))
        trajectory = integrate(midpoint_step, z0, h, steps, model)
        errors.append(np.linalg.norm(trajectory[-1] - exact_conservative(final_time, z0, model)))
        energies = np.array([energy(state, model) for state in trajectory])
        energy_drifts.append(np.max(np.abs(energies - energies[0])))
    slope = float(np.polyfit(np.log(step_sizes), np.log(errors), 1)[0])
    return {
        "observed_order": slope,
        "max_quadratic_energy_drift": float(max(energy_drifts)),
    }


def dissipative_structure_test() -> dict[str, float]:
    model = Oscillator(mass=1.0, stiffness=2.0, damping_rate=0.15)
    z = np.array([0.7, -0.2])
    h = 0.05

    midpoint_jac = finite_difference_jacobian(midpoint_step, z, 0.0, h, model)
    a = model.stiffness * h * h / (4.0 * model.mass)
    rho_h = (1.0 - model.damping_rate * h / 2.0 + a) / (
        1.0 + model.damping_rate * h / 2.0 + a
    )

    strang_jac = finite_difference_jacobian(conformal_strang_step, z, 0.0, h, model)
    exact_factor = np.exp(-model.damping_rate * h)

    z_new = midpoint_step(z, 0.0, h, model)
    p_mid = 0.5 * (z[1] + z_new[1])
    predicted_energy_change = -h * model.damping_rate * p_mid * p_mid / model.mass
    measured_energy_change = energy(z_new, model) - energy(z, model)

    return {
        "midpoint_discrete_conformal_defect": structure_defect(midpoint_jac, rho_h),
        "strang_exact_conformal_defect": structure_defect(strang_jac, exact_factor),
        "midpoint_power_balance_error": abs(measured_energy_change - predicted_energy_change),
    }


def run_all() -> dict[str, object]:
    return {
        "complex_round_trip_error": complex_round_trip(np.array([0.37, -1.2])),
        "conservative": conservative_order_test(),
        "dissipative": dissipative_structure_test(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_all(), indent=2, sort_keys=True))

