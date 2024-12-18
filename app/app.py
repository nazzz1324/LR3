import math

class Shape:
    def __init__(self):
        self._shape_type = "Geometric Shape"

    @staticmethod
    def about():
        print("Программа расчета площади поверхности геометрических фигур.")
        print("Разработано командой из трех человек, а именно Алимов Н.М., Гизулин Т.У. и Валеев А.А.")

    def calculate_surface_area(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")


class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self._shape_type = "Cylinder"
        self.radius = radius
        self.height = height

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self._radius = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self._height = value

    def calculate_surface_area(self):
        # Формула площади поверхности цилиндра: 2πr² + 2πrh
        return 2 * math.pi * self._radius**2 + 2 * math.pi * self._radius * self._height


if __name__ == "__main__":
    Shape.about()
    try:
        radius = float(input("Введите радиус цилиндра: "))
        height = float(input("Введите высоту цилиндра: "))
        cylinder = Cylinder(radius, height)
        surface_area = cylinder.calculate_surface_area()
        print(f"Площадь поверхности цилиндра с радиусом {cylinder.radius} и высотой {cylinder.height} равна {surface_area:.2f}")
    except ValueError as e:
        print(f"Ошибка: {e}")


