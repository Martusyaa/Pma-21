from Figure import Figure
class Square(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side


    def perimeter(self):
        if self.side <= 0:
            raise ValueError("Сторона не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return self.side * 4

    def area(self):
        if self.side <= 0:
            raise ValueError("Сторона не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return self.side**2