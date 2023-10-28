class SomeClass:
    def __init__(self, some: str):
        self.some = some

    def doSmth(self) -> str:
        return "<" + self.some + "!" + ">"
