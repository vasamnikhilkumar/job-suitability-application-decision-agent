import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from model import LIKELIHOODS, PRIORS
from run_simulation import entropy, generate_cases, update


class BeliefModelTests(unittest.TestCase):
    def test_probability_rows(self):
        self.assertTrue(math.isclose(sum(PRIORS.values()), 1.0))
        for check in LIKELIHOODS.values():
            for row in check.values():
                self.assertTrue(math.isclose(sum(row.values()), 1.0))

    def test_documented_update(self):
        posterior = update(PRIORS, "E1_fit", "ambiguous")
        self.assertAlmostEqual(posterior["H2"], 0.43624161073825507)
        self.assertAlmostEqual(entropy(PRIORS) - entropy(posterior), 0.2111925786259654)

    def test_seed_is_reproducible(self):
        self.assertEqual(generate_cases(10, 20260910), generate_cases(10, 20260910))


if __name__ == "__main__":
    unittest.main()
