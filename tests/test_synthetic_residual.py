"""Regression tests for the public-only, fixed, synthetic demonstration."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from synthetic_residual import baseline, describe, generate_samples, mean_residual


class SyntheticResidualTests(unittest.TestCase):
    def test_deterministic_with_fixed_seed(self):
        self.assertEqual(generate_samples(), generate_samples())

    def test_fixed_fixture_size(self):
        self.assertEqual(len(generate_samples()), 80)

    def test_baseline_is_known_and_simple(self):
        self.assertAlmostEqual(baseline(0), 2.0)
        self.assertAlmostEqual(baseline(50), 4.0)

    def test_residual_definition(self):
        for point in generate_samples():
            self.assertAlmostEqual(
                point.residual, point.observed - point.baseline
            )

    def test_inserted_training_effect_is_visible(self):
        self.assertGreater(mean_residual(generate_samples(), 20, 30), 0.90)

    def test_inserted_second_effect_is_visible(self):
        self.assertGreater(mean_residual(generate_samples(), 52, 62), 0.90)

    def test_background_control_stays_small(self):
        self.assertLess(abs(mean_residual(generate_samples(), 35, 45)), 0.20)

    def test_absent_signal_not_misreported_by_fixture(self):
        samples = generate_samples(include_inserted_effect=False)
        self.assertLess(abs(mean_residual(samples, 20, 30)), 0.20)
        self.assertLess(abs(mean_residual(samples, 52, 62)), 0.20)

    def test_window_bounds_fail_closed(self):
        with self.assertRaises(ValueError):
            mean_residual(generate_samples(), 25, 25)

    def test_variable_fixture_count_not_silently_accepted(self):
        with self.assertRaises(ValueError):
            generate_samples(count=40)

    def test_result_explicitly_not_astrophysics(self):
        result = describe(generate_samples())
        self.assertFalse(result["astrophysical_validation"])
        self.assertEqual(result["kind"], "synthetic_teaching_example")


if __name__ == "__main__":
    unittest.main()
