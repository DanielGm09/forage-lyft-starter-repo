from ..tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensor_wear_values : list[float]) -> None:
        super().__init__()
        self.sensor_wear_values = sensor_wear_values

    def needs_service(self) -> bool:
        return sum(self.sensor_wear_values) >= 3