import unittest

from ..serviceable.car.engine.engine import Engine
from ..serviceable.car.engine.models.capulet_engine import CapuletEngine
from ..serviceable.car.engine.models.sternman_engine import SternmanEngine
from ..serviceable.car.engine.models.wiloughby_engine import WiloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced_equal(self):
        engine = CapuletEngine(0, 30_000)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced_greater(self):
        engine = CapuletEngine(10_000, 100_000)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = CapuletEngine(300, 10_000)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_should_not_be(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

class TestWiloughbyEngine(unittest.TestCase):
    def test_should_be_serviced_equal(self):
        engine = WiloughbyEngine(0, 60_000)
        self.assertTrue(engine.needs_service())

    def test_should_be_serviced_greater(self):
        engine = WiloughbyEngine(50_000, 120_000)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = WiloughbyEngine(1000, 60_000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()