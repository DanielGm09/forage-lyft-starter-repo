from ..engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on : bool) -> None:
        super().__init__()
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on