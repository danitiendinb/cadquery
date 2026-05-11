"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is a Python library that allows you to build 3D models with
scripts. It is a fork of the original CadQuery project, built on top
of Open CASCADE Technology (OCCT) via the python-occ (OCC) bindings.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)

See also:
    - https://cadquery.readthedocs.io for full documentation
    - https://github.com/CadQuery/cadquery for the upstream project

Personal fork notes:
    - Tracking upstream v2.4.0
    - Using this fork to experiment with custom selectors and assembly workflows
    - Added cq.box() and cq.sphere() convenience helpers at module level
    - Added cq.cylinder() convenience helper
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


# --- Personal convenience helpers ---
# Quick shorthand functions so I don't have to type Workplane("XY") every time.

def box(length, width, height):
    """Shorthand for cq.Workplane('XY').box(length, width, height)."""
    return Workplane("XY").box(length, width, height)


def sphere(radius):
    """Shorthand for cq.Workplane('XY').sphere(radius)."""
    return Workplane("XY").sphere(radius)


def cylinder(radius, height, centered=True):
    """Shorthand for cq.Workplane('XY').cylinder(height, radius).

    Note: CadQuery's cylinder() takes height then radius, but I find
    radius-first more intuitive, so this wrapper swaps the order.
    """
    return Workplane("XY").cylinder(height, radius, centered=centered)


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
    # Personal helpers
    "box",
    "sphere",
    "cylinder",
]
