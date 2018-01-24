import unittest
import numpy as np

from standard_similarity import average_similarity


class SimilarityCalculator(unittest.TestCase):
    def test_averageSimilarity_withMultipleSimilarity_shouldReturnAverageOfThem(self):
        similarities = np.asarray([[1, 1], [2, 2]])

        self.assertEquals([1.5, 1.5], list(average_similarity(similarities)))
