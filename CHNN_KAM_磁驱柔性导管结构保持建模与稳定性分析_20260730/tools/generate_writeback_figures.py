"""Generate manuscript figures from frozen, lightweight evidence tables.

This script performs no simulation or experiment.  It reads only the two CSV
files committed under figures/data and writes deterministic PDF/PNG figures.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "figures" / "data"
OUT = ROOT / "figures"

BLUE = "#0072B2"
ORANGE = "#D55E00"
GREEN = "#009E73"
GRAY = "#4D4D4D"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def save_figure(fig: plt.Figure, stem: str) -> None:
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", dpi=240, bbox_inches="tight")
    plt.close(fig)


def bridge_gate_figure() -> None:
    rows = read_csv(DATA / "bridge_gate_separation.csv")
    names = [row["trajectory"] for row in rows]
    energy = np.array([float(row["energy_drift_percent"]) for row in rows])
    force = np.array([float(row["force_v2_joint_l2_percent"]) for row in rows])
    strict = float(rows[0]["strict_energy_threshold_percent"])
    candidate = float(rows[0]["candidate_energy_threshold_percent"])
    force_threshold = float(rows[0]["force_v2_threshold_percent"])
    x = np.arange(len(names))

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3), constrained_layout=True)

    axes[0].bar(x, energy, color=BLUE, edgecolor="black", linewidth=0.6)
    axes[0].axhline(strict, color=ORANGE, linestyle="--", linewidth=1.5, label="strict 0.5%")
    axes[0].axhline(candidate, color=GREEN, linestyle=":", linewidth=1.8, label="candidate 1%")
    axes[0].set_title("(a) Perturbation-energy drift")
    axes[0].set_ylabel("Peak-to-peak drift (%)")
    axes[0].set_xticks(x, names)
    axes[0].set_ylim(0, 1.08)
    axes[0].legend(frameon=False, fontsize=8, loc="upper right")
    for index, value in enumerate(energy):
        axes[0].text(index, value + 0.025, f"{value:.3f}", ha="center", va="bottom", fontsize=8)

    axes[1].bar(x, force, color=ORANGE, edgecolor="black", linewidth=0.6)
    axes[1].axhline(force_threshold, color=GRAY, linestyle="--", linewidth=1.5, label="force-v2 2%")
    axes[1].set_title("(b) Force-v2 closure")
    axes[1].set_ylabel("Joint relative L2 (%)")
    axes[1].set_xticks(x, names)
    axes[1].set_ylim(0, 2.22)
    axes[1].legend(frameon=False, fontsize=8, loc="upper right")
    for index, value in enumerate(force):
        axes[1].text(index, value + 0.055, f"{value:.3f}", ha="center", va="bottom", fontsize=8)

    for axis in axes:
        axis.spines["top"].set_visible(False)
        axis.spines["right"].set_visible(False)
        axis.grid(axis="y", color="#D9D9D9", linewidth=0.6, alpha=0.8)
        axis.set_axisbelow(True)

    save_figure(fig, "fig_bridge_gate_separation")


def convergence_order_figure() -> None:
    rows = read_csv(DATA / "b0_r2_convergence_orders.csv")
    labels = [r"$q$", r"$p_{\mathrm{proj}}$", r"$M_N^{-1}p$", r"$B^\mathsf{T}L$", "energy"]
    values = np.array([float(row["observed_order"]) for row in rows])
    x = np.arange(len(labels))

    fig, axis = plt.subplots(figsize=(6.7, 3.6), constrained_layout=True)
    colors = [BLUE, BLUE, BLUE, BLUE, GREEN]
    axis.bar(x, values, color=colors, edgecolor="black", linewidth=0.6)
    axis.axhline(1.0, color=GRAY, linestyle="--", linewidth=1.2, label="first order")
    axis.axhline(2.0, color=ORANGE, linestyle=":", linewidth=1.5, label="second order")
    axis.set_ylabel("Observed order")
    axis.set_xticks(x, labels)
    axis.set_ylim(0, 2.22)
    axis.grid(axis="y", color="#D9D9D9", linewidth=0.6, alpha=0.8)
    axis.set_axisbelow(True)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.legend(frameon=False, fontsize=8, loc="lower right")
    for index, value in enumerate(values):
        axis.text(index, value + 0.035, f"{value:.3f}", ha="center", va="bottom", fontsize=8)

    save_figure(fig, "fig_b0_r2_convergence_orders")


def main() -> None:
    bridge_gate_figure()
    convergence_order_figure()


if __name__ == "__main__":
    main()
