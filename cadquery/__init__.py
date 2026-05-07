"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is a Python library that allows you to build 3D models with
scripts. It is a fork of the original CadQuery project, built on top
of Open CASCADE Technology (OCCT) via the python-occ (OCC) bindings.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    Location,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .assembly import (
    Assembly,
    Constraint,
)
from .sketch import Sketch
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    CenterNthSelector,
    RadiusNthSelector,
    LengthNthSelector,
    SumSelector,
    SubtractSelector,
    AndSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from . import exporters
from . import importers

__version__ = "2.4.0"

__all__ = [
    # Core workplane
    "CQContext",
    "CQObject",
    "Workplane",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shape types
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Assembly
    "Assembly",
    "Constraint",
    # Sketch
    "Sketch",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "CenterNthSelector",
    "RadiusNthSelector",
    "LengthNthSelector",
    "SumSelector",
    "SubtractSelector",
    "AndSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Modules
    "exporters",
    "importers",
]
