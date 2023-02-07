import unittest

from ..serviceable.car.tires.tires import Tires
from ..serviceable.car.tires.models.carrigan_tires import CarriganTires
from ..serviceable.car.tires.models.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced_equal_single_idx_one(self):
        tires = CarriganTires([0.9, 0.3, 0.2, 0.8])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_equal_single_idx_three(self):
        tires = CarriganTires([0.1, 0.2, 0.9, 0.3])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_equal_multiple(self):
        tires = CarriganTires([0.1, 0.9, 0.2, 0.9])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_greater_single_idx_one(self):
        tires = CarriganTires([0.98, 0.3, 0.6, 0.89])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_greater_single_idx_three(self):
        tires = CarriganTires([0.2, 0.35, 0.92, 0])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_greater_multiple(self):
        tires = CarriganTires([0.98, 0.1, 0.99, 1])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = CarriganTires([0.1, 0, 0.89, 0.75])
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_should_be_serviced_equal(self):
        tires = OctoprimeTires([0.75, 0.5, 1, 0.75])
        self.assertTrue(tires.needs_service())

    def test_should_be_serviced_greater(self):
        tires = OctoprimeTires([0.9, 0.9, 0.8, 0.75])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = OctoprimeTires([0, 1, 0.5, 0.75])
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()