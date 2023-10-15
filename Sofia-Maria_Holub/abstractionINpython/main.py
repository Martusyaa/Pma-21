class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"{self.color.fill_color()} {self.get_shape_name()}"

    def get_shape_name(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def get_shape_name(self):
        return "circle"

    def calculate_area(self, radius):
        return 3.14 * radius * radius

    def calculate_perimeter(self, radius):
        return 2 * 3.14 * radius

class Rectangle(Shape):
    def get_shape_name(self):
        return "rectangle"

    def calculate_area(self, width, height):
        return width * height

    def calculate_perimeter(self, width, height):
        return 2 * (width + height)

class Square(Shape):
    def get_shape_name(self):
        return "square"

    def calculate_area(self, side):
        return side * side

    def calculate_perimeter(self, side):
        return 4 * side

class Color:
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        return "Red"

class BlueColor(Color):
    def fill_color(self):
        return "Blue"

class GreenColor(Color):
    def fill_color(self):
        return "Green"


def read_figures_from_file(filename):
    figures = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                shape_type = parts[0].strip()
                color = parts[1].strip()
                if shape_type == "Circle":
                    radius = float(parts[2].strip())
                    figures.append(Circle(get_color(color)))
                elif shape_type == "Rectangle":
                    width = float(parts[2].strip())
                    height = float(parts[3].strip())
                    figures.append(Rectangle(get_color(color)))
                elif shape_type == "Square":
                    side = float(parts[2].strip())
                    figures.append(Square(get_color(color)))
    return figures


def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            file.write(result + '\n')


def get_color(color_name):
    if color_name == "Red":
        return RedColor()
    elif color_name == "Blue":
        return BlueColor()
    elif color_name == "Green":
        return GreenColor()


input_filename = "input.txt"
output_filename = "output.txt"
figures = read_figures_from_file(input_filename)


results = []
for figure in figures:
    if isinstance(figure, Circle):
        area = figure.calculate_area(8)
        results.append(f"{figure.draw()}: Area = {area}")
    elif isinstance(figure, Rectangle):
        perimeter = figure.calculate_perimeter(7, 6)
        results.append(f"{figure.draw()}: Perimeter = {perimeter}")
    elif isinstance(figure, Square):
        area = figure.calculate_area(4)
        results.append(f"{figure.draw()}: Area = {area}")

write_results_to_file(output_filename, results)
