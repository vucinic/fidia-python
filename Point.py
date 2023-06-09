class Point:

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise Exception('Operazione mista')
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    def __add__(self, other):
        if not isinstance(other, Point):
            raise Exception('Operazione mista')
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __lt__(self, other):
        if not isinstance(other, Point):
            raise Exception('Operazione mista')
        return self.distance_from(Point()) < other.distance_from(Point())

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise Exception('Operazione mista')
        return self.distance_from(Point()) > other.distance_from(Point())

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise Exception('Operazione mista')
        return self.distance_from(Point(0, 0)) == other.distance_from(Point(0, 0))

    def distance_from(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def triangle_area(self):
        return (self.x * self.y) / 2
