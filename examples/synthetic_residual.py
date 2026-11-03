#!/usr/bin/env python3
"""A reproducible public illustration of a residual—not dark-matter research.

Everything here is synthetic. The baseline, added effect and test windows are
specified by the author of the fixture. No astronomical model, hidden-cause
inference or claim of detection is present.
"""
from __future__ import annotations

import json
import random
from typing import NamedTuple


class Sample(NamedTuple):
    index: int
    baseline: float
    observed: float
    residual: float


def baseline(index: int) -> float:
    """A simple, known reference curve for the fabricated example."""
    return 2.0 + 0.04 * index


def generate_samples(
    count: int = 80,
    seed: int = 2026,
    include_inserted_effect: bool = True,
) -> list[Sample]:
    """Generate synthetic data with bounded noise and two preselected windows."""
    if count != 80:
        raise ValueError("This fixed educational fixture requires count=80.")
    random_generator = random.Random(seed)
    samples: list[Sample] = []
    for index in range(count):
        reference = baseline(index)
        noise = random_generator.uniform(-0.20, 0.20)
        # The observer knows these windows because we constructed the data.
        repeated_effect = (
            1.20
            if include_inserted_effect and (20 <= index < 30 or 52 <= index < 62)
            else 0.0
        )
        observed = reference + noise + repeated_effect
        samples.append(
            Sample(
                index=index,
                baseline=reference,
                observed=observed,
                residual=observed - reference,
            )
        )
    return samples


def mean_residual(samples: list[Sample], start: int, end: int) -> float:
    """Simple descriptive statistic, not a significance or physics test."""
    if not (0 <= start < end <= len(samples)):
        raise ValueError("Invalid fixed observation window.")
    return sum(s.residual for s in samples[start:end]) / (end - start)


def describe(samples: list[Sample]) -> dict[str, object]:
    return {
        "kind": "synthetic_teaching_example",
        "sample_count": len(samples),
        "train_window_mean_residual": round(mean_residual(samples, 20, 30), 5),
        "withheld_window_mean_residual": round(mean_residual(samples, 52, 62), 5),
        "control_window_mean_residual": round(mean_residual(samples, 35, 45), 5),
        "interpretation": (
            "Inserted effects were known by construction. "
            "Residuals do not identify a physical cause."
        ),
        "astrophysical_validation": False,
    }


if __name__ == "__main__":
    print(json.dumps(describe(generate_samples()), indent=2, sort_keys=True))
