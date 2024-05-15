class TestModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.key = f"{name}:{value}"

    def dict(self):
        return {"name": self.name, "value": self.value}