from ..tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensor_wear_values : list[float]) -> None:
        super().__init__()
        self.sensor_wear_values = sensor_wear_values

    def needs_service(self) -> bool:
        for wear_value in self.sensor_wear_values:
            if wear_value >= 0.9:
                return True
        return False