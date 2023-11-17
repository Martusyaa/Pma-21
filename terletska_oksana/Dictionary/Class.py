class Garden:
    def __init__(self, type_of_plant, color, height):
        self.type_of_plant = type_of_plant
        self.color = color
        self.height = height

    def __str__(self):
        return f" {self.type_of_plant} {self.color} {self.height} "
