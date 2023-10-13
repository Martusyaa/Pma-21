from Figurs.Figure import Figure
class Rectangle(Figure):
    def __init__(self, color, sideA, sideB, sideC, sideD):
        super().__init__(color)
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
        self.sideD = sideD


    def perimeter(self):
        if self.sideA <= 0 or self.sideB <= 0 or self.sideC <= 0 or self.sideD <= 0:
            raise ValueError("Сторона не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return self.sideA+self.sideB+self.sideC+self.sideD

    def area(self):
        if self.sideA <= 0 or self.sideB <= 0 or self.sideC <= 0 or self.sideD <= 0:
            raise ValueError("Сторона не може дорівнювати 0 чи бути меншою за 1!")
        else:
            return self.sideA*self.sideB