from ..serviceable import Serviceable
from datetime import date

# Engine Imports
from .engine.engine import Engine
from .engine.models.capulet_engine import CapuletEngine
from .engine.models.sternman_engine import SternmanEngine
from .engine.models.wiloughby_engine import WiloughbyEngine

# Battery Imports
from .battery.battery import Battery
from .battery.models.spindler_battery import SpinderBattery
from .battery.models.nubbin_battery import NubinBattery

class Car(Serviceable):
    def __init__(self, engine : Engine, battery : Battery) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory():
    def create_calliope(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpinderBattery(last_service_date, current_date))

    def create_glissade(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(WiloughbyEngine(last_service_mileage, current_mileage), SpinderBattery(last_service_date, current_date))

    def create_palindrome(current_date : date, last_service_date : date, warning_light_on : bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpinderBattery(last_service_date, current_date))

    def create_rorschach(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(WiloughbyEngine(last_service_mileage, current_mileage), NubinBattery(last_service_date, current_date))

    def create_thovex(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubinBattery(last_service_date, current_date))