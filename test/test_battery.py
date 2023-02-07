import unittest
from datetime import datetime, timedelta

from ..serviceable.car.battery.battery import Battery
from ..serviceable.car.battery.models.spindler_battery import SpindlerBattery
from ..serviceable.car.battery.models.nubbin_battery import NubinBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced_equal(self):
        today = datetime.utcnow().date()
        battery = SpindlerBattery(today, today + timedelta(days=365.25*2))
        self.assertTrue(battery.needs_service())

    def test_should_be_serviced_greater(self):
        today = datetime.utcnow().date()
        battery = SpindlerBattery(today, today + timedelta(days=365.25*10))
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.utcnow().date()
        battery = SpindlerBattery(today, today + timedelta(days=365.25*1.25))
        self.assertFalse(battery.needs_service())

class TestNubinBattery(unittest.TestCase):
    def test_should_be_serviced_equal(self):
        today = datetime.utcnow().date()
        battery = NubinBattery(today, today + timedelta(days=365.25*4))
        self.assertTrue(battery.needs_service())

    def test_should_be_serviced_greater(self):
        today = datetime.utcnow().date()
        battery = NubinBattery(today, today + timedelta(days=365.25*8))
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.utcnow().date()
        battery = NubinBattery(today, today + timedelta(days=365.25*2))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()