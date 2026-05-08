"""Core geometric shape primitives for CadQuery.

This module provides the fundamental 3D shape classes that serve as
building blocks for more complex models.
"""

from typing import Optional, Tuple
import math


class Vector:
    """A 3D vector or point in space."""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self) -> float:
        """Return the Euclidean length of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        l = self.length()
        if l == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / l, self.y / l, self.z / l)

    def dot(self, other: "Vector") -> float:
        """Compute the dot product with another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector") -> "Vector":
        """Compute the cross product with another vector."""
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def to_tuple(self) -> Tuple[float, float, float]:
        """Return the vector as a (x, y, z) tuple."""
        return (self.x, self.y, self.z)


class Shape:
    """Base class for all CadQuery geometric shapes."""

    def __init__(self):
        self._center = Vector(0.0, 0.0, 0.0)

    @property
    def center(self) -> Vector:
        """Return the center of mass / centroid of the shape."""
        return self._center

    def volume(self) -> float:
        """Return the volume of the shape. Subclasses must override."""
        raise NotImplementedError

    def surface_area(self) -> float:
        """Return the surface area of the shape. Subclasses must override."""
        raise NotImplementedError

    def translate(self, vec: Vector) -> "Shape":
        """Return a translated copy of this shape."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(center={self._center})"


class Box(Shape):
    """An axis-aligned rectangular box (cuboid)."""

    def __init__(
        self,
        length: float,
        width: float,
        height: float,
        center: Optional[Vector] = None,
    ):
        super().__init__()
        if any(d <= 0 for d in (length, width, height)):
            raise ValueError("Box dimensions must be positive")
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)
        self._center = center if center is not None else Vector(0.0, 0.0, 0.0)

    def volume(self) -> float:
        return self.length * self.width * self.height

    def surface_area(self) -> float:
        return 2 * (
            self.length * self.width
            + self.width * self.height
            + self.height * self.length
        )

    def translate(self, vec: Vector) -> "Box":
        return Box(self.length, self.width, self.height, self._center + vec)

    def __repr__(self) -> str:
        return (
            f"Box(length={self.length}, width={self.width}, "
            f"height={self.height}, center={self._center})"
        )


class Sphere(Shape):
    """A sphere defined by its radius."""

    def __init__(self, radius: float, center: Optional[Vector] = None):
        super().__init__()
        if radius <= 0:
            raise ValueError("Sphere radius must be positive")
        self.radius = float(radius)
        self._center = center if center is not None else Vector(0.0, 0.0, 0.0)

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius ** 3

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def translate(self, vec: Vector) -> "Sphere":
        return Sphere(self.radius, self._center + vec)

    def __repr__(self) -> str:
        return f"Sphere(radius={self.radius}, center={self._center})"
