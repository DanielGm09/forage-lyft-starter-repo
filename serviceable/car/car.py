from ..serviceable import Serviceable
from datetime import date

# Engine Imports
from .engine.engine import Engine
from .engine.models.capulet_engine import CapuletEngine
from .engine.models.sternman_engine import SternmanEngine
from .engine.models.wiloughby_engine import WiloughbyEngine

# Battery Imports
from .battery.battery import Battery
from .battery.models.spindler_battery import SpindlerBattery
from .battery.models.nubbin_battery import NubinBattery

# Tire Imports
from .tires.tires import Tires
from .tires.models.carrigan_tires import CarriganTires
from .tires.models.octoprime_tires import OctoprimeTires

class Car(Serviceable):
    def __init__(self, engine : Engine, battery : Battery, tires: Tires) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory():
    # It is not clear which tires are applied to which Lyft vehicles, they have been applied in an alternating fashion
    def create_calliope(self,
        current_date : date, 
        last_service_date : date, 
        current_mileage : int, 
        last_service_mileage : int,
        sensor_wear_values : list[float]) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(sensor_wear_values))

    def create_glissade(self,
        current_date : date, 
        last_service_date : date, 
        current_mileage : int, 
        last_service_mileage : int,
        sensor_wear_values : list[float]) -> Car:
        return Car(WiloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTires(sensor_wear_values))

    def create_palindrome(self,
        current_date : date, 
        last_service_date : date, 
        warning_light_on : bool,
        sensor_wear_values : list[float]) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTires(sensor_wear_values))

    def create_rorschach(self,
        current_date : date, 
        last_service_date : date, 
        current_mileage : int, 
        last_service_mileage : int,
        sensor_wear_values : list[float]) -> Car:
        return Car(WiloughbyEngine(last_service_mileage, current_mileage), NubinBattery(last_service_date, current_date), OctoprimeTires(sensor_wear_values))

    def create_thovex(self,
        current_date : date, 
        last_service_date : date, 
        current_mileage : int, 
        last_service_mileage : int,
        sensor_wear_values : list[float]) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubinBattery(last_service_date, current_date), CarriganTires(sensor_wear_values))