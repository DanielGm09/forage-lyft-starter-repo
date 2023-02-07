from ..battery import Battery
from datetime import date, timedelta

class SpindlerBattery(Battery):
    def __init__(self, last_service_date : date, current_date : date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        years_in_days = 3*365.25
        return self.last_service_date + timedelta(days=years_in_days) <= self.current_date
    