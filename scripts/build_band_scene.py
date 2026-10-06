"""Build a compact WTG stage mesh for GitHub's native STL viewer."""

from collections import Counter
from math import cos, pi, sin, sqrt
from pathlib import Path
import re
from xml.etree import ElementTree

Vec2 = tuple[float, float]
Vec3 = tuple[float, float, float]
Triangle = tuple[Vec3, Vec3, Vec3]


def add(a: Vec3, b: Vec3) -> Vec3:
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def sub(a: Vec3, b: Vec3) -> Vec3:
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def scale(a: Vec3, amount: float) -> Vec3:
    return a[0] * amount, a[1] * amount, a[2] * amount


def cross(a: Vec3, b: Vec3) -> Vec3:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def unit(a: Vec3) -> Vec3:
    length = sqrt(sum(value * value for value in a))
    if length < 1e-10:
        raise ValueError("Zero-length geometry vector")
    return scale(a, 1 / length)


def area(points: list[Vec2]) -> float:
    return (
        sum(
            a[0] * b[1] - b[0] * a[1]
            for a, b in zip(points, points[1:] + points[:1], strict=True)
        )
        / 2
    )


def turn(a: Vec2, b: Vec2, c: Vec2) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def triangulate(points: list[Vec2]) -> list[tuple[int, int, int]]:
    # ponytail: ear clipping for small contours; use a tessellator for complex logos.
    remaining = list(range(len(points)))
    triangles: list[tuple[int, int, int]] = []
    while len(remaining) > 3:
        for position, current in enumerate(remaining):
            previous = remaining[position - 1]
            following = remaining[(position + 1) % len(remaining)]
            a, b, c = points[previous], points[current], points[following]
            if turn(a, b, c) <= 1e-8:
                continue
            if any(
                turn(a, b, points[index]) >= -1e-8
                and turn(b, c, points[index]) >= -1e-8
                and turn(c, a, points[index]) >= -1e-8
                for index in remaining
                if index not in (previous, current, following)
            ):
                continue
            triangles.append((previous, current, following))
            remaining.pop(position)
            break
        else:
            raise ValueError("Cannot triangulate logo contour")
    triangles.append((remaining[0], remaining[1], remaining[2]))
    return triangles


def prism(
    points: list[Vec2],
    depth: float,
    origin: Vec3,
    u: Vec3 = (1, 0, 0),
    v: Vec3 = (0, 1, 0),
    w: Vec3 = (0, 0, 1),
) -> list[Triangle]:
    points = points if area(points) > 0 else points[::-1]
    vertices = [
        add(origin, add(scale(u, x), add(scale(v, y), scale(w, z))))
        for z in (0, depth)
        for x, y in points
    ]
    count = len(points)
    faces: list[tuple[int, int, int]] = []
    for a, b, c in triangulate(points):
        faces.extend(((a, c, b), (count + a, count + b, count + c)))
    for index in range(count):
        following = (index + 1) % count
        faces.extend(
            (
                (index, following, count + following),
                (index, count + following, count + index),
            )
        )
    return [(vertices[a], vertices[b], vertices[c]) for a, b, c in faces]


def box(center: Vec3, size: Vec3) -> list[Triangle]:
    x, y, z = size
    return prism(
        [(-x / 2, -y / 2), (x / 2, -y / 2), (x / 2, y / 2), (-x / 2, y / 2)],
        z,
        sub(center, (0, 0, z / 2)),
    )


def cylinder(
    start: Vec3,
    end: Vec3,
    radius: float,
    sides: int = 6,
    end_radius: float | None = None,
) -> list[Triangle]:
    axis = unit(sub(end, start))
    reference: Vec3 = (0, 1, 0) if abs(axis[2]) > 0.9 else (0, 0, 1)
    u = unit(cross(reference, axis))
    v = cross(axis, u)
    top_radius = radius if end_radius is None else end_radius
    bottom = [
        add(
            start,
            add(
                scale(u, radius * cos(2 * pi * i / sides)),
                scale(v, radius * sin(2 * pi * i / sides)),
            ),
        )
        for i in range(sides)
    ]
    top = [
        add(
            end,
            add(
                scale(u, top_radius * cos(2 * pi * i / sides)),
                scale(v, top_radius * sin(2 * pi * i / sides)),
            ),
        )
        for i in range(sides)
    ]
    mesh: list[Triangle] = []
    for i in range(sides):
        j = (i + 1) % sides
        mesh.extend(
            (
                (bottom[i], bottom[j], top[j]),
                (bottom[i], top[j], top[i]),
                (start, bottom[j], bottom[i]),
                (end, top[i], top[j]),
            )
        )
    return mesh


def svg_contours(path: Path) -> list[list[Vec2]]:
    root = ElementTree.parse(path).getroot()
    contours: list[list[Vec2]] = []
    for element in root.findall(".//{http://www.w3.org/2000/svg}path"):
        data = element.get("d", "")
        if set(re.findall(r"[A-DF-Za-df-z]", data)) - set("MmLlHhVvCcSsZz"):
            raise ValueError("Unsupported SVG path command")
        tokens = re.findall(
            r"[MmLlHhVvCcSsZz]|[-+]?(?:\d*\.?\d+)(?:[Ee][-+]?\d+)?", data
        )
        position = 0
        command = ""
        current: Vec2 = (0, 0)
        start: Vec2 = (0, 0)
        contour: list[Vec2] = []
        previous_control: Vec2 | None = None
        while position < len(tokens):
            if tokens[position].isalpha():
                command = tokens[position]
                position += 1
            if command in ("Z", "z"):
                if contour and contour[-1] == contour[0]:
                    contour.pop()
                contours.append(contour)
                contour = []
                current = start
                command = ""
                previous_control = None
                continue
            sizes = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4}
            count = sizes.get(command.upper())
            if count is None:
                raise ValueError("Malformed SVG path")
            values = [float(value) for value in tokens[position : position + count]]
            if len(values) != count:
                raise ValueError("Incomplete SVG command")
            position += count
            relative = command.islower()
            if command.upper() in ("M", "L"):
                target: Vec2 = (
                    values[0] + (current[0] if relative else 0),
                    values[1] + (current[1] if relative else 0),
                )
                if command.upper() == "M":
                    if contour:
                        contours.append(contour)
                    contour = []
                    start = target
                    command = "l" if relative else "L"
                current = target
                contour.append(current)
                previous_control = None
            elif command.upper() == "H":
                current = (values[0] + (current[0] if relative else 0), current[1])
                contour.append(current)
                previous_control = None
            elif command.upper() == "V":
                current = (current[0], values[0] + (current[1] if relative else 0))
                contour.append(current)
                previous_control = None
            else:
                offset = current if relative else (0, 0)
                controls = [
                    (values[i] + offset[0], values[i + 1] + offset[1])
                    for i in range(0, count, 2)
                ]
                if command.upper() == "S":
                    reflected = (
                        current
                        if previous_control is None
                        else (
                            2 * current[0] - previous_control[0],
                            2 * current[1] - previous_control[1],
                        )
                    )
                    controls.insert(0, reflected)
                for sample in range(1, 5):
                    t = sample / 4
                    coordinates = [
                        (1 - t) ** 3 * current[axis]
                        + 3 * (1 - t) ** 2 * t * controls[0][axis]
                        + 3 * (1 - t) * t * t * controls[1][axis]
                        + t**3 * controls[2][axis]
                        for axis in (0, 1)
                    ]
                    contour.append((coordinates[0], coordinates[1]))
                current = controls[2]
                previous_control = controls[1]
        if contour:
            contours.append(contour)
    # ponytail: bounded contour simplification for a compact README mesh.
    for contour in contours:
        changed = True
        while changed and len(contour) > 3:
            changed = False
            for index, point in enumerate(contour):
                a, b = contour[index - 1], contour[(index + 1) % len(contour)]
                length = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
                if length > 1e-8 and abs(turn(a, b, point)) / length < 5:
                    contour.pop(index)
                    changed = True
                    break
    return contours


def guitar(x: float, y: float, z: float, bass: bool = False) -> list[Triangle]:
    outline = [
        (-0.42, -0.38),
        (-0.54, -0.08),
        (-0.36, 0.12),
        (-0.30, 0.42),
        (-0.15, 0.28),
        (0, 0.15),
        (0.18, 0.31),
        (0.32, 0.48),
        (0.34, 0.16),
        (0.53, -0.08),
        (0.4, -0.4),
        (0, -0.52),
    ]
    mesh = prism(outline, 0.12, (x, y, z), (1, 0, 0.1), (0, 0, 1), (0, -1, 0))
    neck_length = 1.2 if bass else 1.0
    mesh += box((x, y - 0.06, z + 0.1 + neck_length / 2), (0.12, 0.10, neck_length))
    mesh += box((x, y - 0.07, z + 0.1 + neck_length + 0.15), (0.24, 0.11, 0.3))
    mesh += box((x, y - 0.14, z - 0.20), (0.28, 0.08, 0.08))
    for pickup in (-0.02, 0.15):
        mesh += box((x, y - 0.14, z + pickup), (0.30, 0.05, 0.08))
    for index in range(4 if bass else 6):
        offset = (index - (1.5 if bass else 2.5)) * 0.018
        mesh += cylinder(
            (x + offset, y - 0.18, z - 0.25),
            (x + offset, y - 0.18, z + 0.1 + neck_length + 0.23),
            0.005,
            3,
        )
    for index in range(5):
        mesh += box(
            (x, y - 0.125, z + 0.13 + index * neck_length / 5), (0.15, 0.025, 0.015)
        )
    for side in (-1, 1):
        mesh += cylinder(
            (x + side * 0.10, y - 0.07, z + 0.17 + neck_length),
            (x + side * 0.22, y - 0.07, z + 0.17 + neck_length),
            0.045,
            4,
        )
    mesh += cylinder((x, y + 0.1, 0.12), (x, y + 0.1, z + 0.5), 0.035, 4)
    for side in (-1, 1):
        mesh += cylinder((x, y + 0.1, 0.14), (x + side * 0.35, y - 0.2, 0.05), 0.025, 3)
        mesh += cylinder(
            (x, y + 0.1, z - 0.5), (x + side * 0.25, y - 0.15, z - 0.5), 0.025, 3
        )

    def pose(vertex: Vec3) -> Vec3:
        return 2 * x - vertex[0], 2 * y - vertex[1], vertex[2]

    return [(pose(a), pose(b), pose(c)) for a, b, c in mesh]


def mesa_badge(center: Vec3) -> list[Triangle]:
    glyphs: list[list[list[Vec2]]] = [
        [[(0, 0), (0, 1), (0.3, 0.5), (0.6, 1), (0.6, 0)]],
        [[(0.6, 1), (0, 1), (0, 0), (0.6, 0)], [(0, 0.5), (0.5, 0.5)]],
        [[(0.6, 1), (0, 1), (0, 0.5), (0.6, 0.5), (0.6, 0), (0, 0)]],
        [[(0, 0), (0.3, 1), (0.6, 0)], [(0.15, 0.5), (0.45, 0.5)]],
    ]
    mesh: list[Triangle] = []
    for index, paths in enumerate(glyphs):
        for points in paths:
            for a, b in zip(points, points[1:]):
                start = add(
                    center, ((index * 0.85 + a[0] - 1.575) * 0.22, 0, a[1] * 0.22)
                )
                end = add(
                    center, ((index * 0.85 + b[0] - 1.575) * 0.22, 0, b[1] * 0.22)
                )
                mesh += cylinder(start, end, 0.015, 4)
    return mesh


def amplifiers() -> list[Triangle]:
    # Mesa Dual Rectifier-style head and 4x12 cabinet.
    mesh = box((-4.7, -2.05, 0.91), (1.7, 0.85, 1.7))
    mesh += box((-4.7, -2.05, 2.02), (1.7, 0.75, 0.38))
    mesh += box((-4.7, -1.66, 2.02), (1.56, 0.04, 0.28))
    for x in (-5.13, -4.27):
        for z in (0.49, 1.27):
            mesh += cylinder((x, -1.61, z), (x, -1.55, z), 0.34, 8, end_radius=0.30)
    for index in range(9):
        x = -5.34 + index * 0.13
        mesh += cylinder((x, -1.62, 1.99), (x, -1.56, 1.99), 0.037, 4)
    mesh += box((-4.07, -1.60, 2.01), (0.08, 0.07, 0.11))
    mesh += box((-4.7, -2.05, 2.24), (0.45, 0.14, 0.06))
    mesh += mesa_badge((-4.7, -1.55, 1.53))
    # Separate SVT-style bass head and 8x10 cabinet.
    mesh += box((4.8, -2.05, 1.15), (1.25, 0.9, 2.25))
    mesh += box((4.8, -2.05, 2.50), (1.3, 0.75, 0.4))
    for x in (4.5, 5.1):
        for z in (0.32, 0.86, 1.40, 1.94):
            mesh += cylinder((x, -1.59, z), (x, -1.54, z), 0.23, 6, end_radius=0.20)
    for x in (4.3, 4.6, 4.9, 5.2):
        mesh += cylinder((x, -1.66, 2.47), (x, -1.60, 2.47), 0.055, 6)
    mesh += box((4.8, -2.05, 2.73), (0.40, 0.14, 0.06))
    for x in (4.18, 5.42):
        mesh += box((x, -2.05, 1.45), (0.04, 0.3, 0.16))
    return mesh


def build_scene(logo: Path) -> list[Triangle]:
    mesh = box((0, 0, -0.2), (15, 8, 0.4)) + box((0, -1.8, 0.12), (5.4, 3.2, 0.24))
    mesh += box((0, -3.6, 4.45), (7, 0.16, 3.5))
    scale_logo = 3 / 1504
    contours = svg_contours(logo)
    if not contours:
        raise ValueError("WTG monogram has no path contours")
    for contour in contours:
        points = [((x - 498) * scale_logo, (y - 498) * scale_logo) for x, y in contour]
        mesh += prism(
            points,
            0.13,
            (-1040 * scale_logo / 2, -3.48, 6.0),
            (1, 0, 0),
            (0, 0, -1),
            (0, 1, 0),
        )
    mesh += guitar(-3.3, 0.8, 0.70)
    mesh += guitar(3.3, 0.8, 0.70, bass=True)
    mesh += cylinder((0, 1.7, 0), (0, 1.7, 2.20), 0.035, 4)
    mesh += cylinder((0, 1.7, 2.20), (0, 2.0, 2.36), 0.028, 4)
    mesh += cylinder((0, 2.0, 2.36), (0, 2.22, 2.39), 0.055, 6)
    mesh += cylinder((0, 2.22, 2.39), (0, 2.30, 2.40), 0.08, 8)
    for angle in (0, 2 * pi / 3, 4 * pi / 3):
        mesh += cylinder(
            (0, 1.7, 0.15),
            (0.45 * cos(angle), 1.7 + 0.45 * sin(angle), 0.03),
            0.025,
            3,
        )
    mesh += cylinder((0, -0.7, 0.85), (0, 0.08, 0.85), 0.70, 10)
    mesh += cylinder((0, 0.08, 0.85), (0, 0.11, 0.85), 0.72, 10)
    mesh += box((0.18, 0.46, 0.12), (0.14, 0.38, 0.10))
    mesh += box((-0.32, 0.46, 0.12), (0.14, 0.38, 0.10))
    mesh += cylinder((-0.32, 0.30, 0.20), (0.18, 0.30, 0.20), 0.025, 4)
    for side in (-1, 1):
        mesh += cylinder(
            (side * 0.52, -0.45, 0.45), (side * 0.78, -0.12, 0.12), 0.03, 4
        )
    for x, y, z, radius, height in (
        (-0.52, -0.58, 1.5, 0.31, 0.4),
        (0.52, -0.58, 1.5, 0.31, 0.4),
        (-0.85, -1.12, 1.05, 0.36, 0.22),
        (1.0, -1.6, 0.84, 0.43, 0.58),
    ):
        mesh += cylinder((x, y, z), (x, y, z + height), radius, 8)
        mesh += cylinder(
            (x, y, z + height), (x, y, z + height + 0.04), radius + 0.025, 8
        )
        mesh += cylinder((x, y, 0.2), (x, y, z), 0.03, 4)
    mesh += cylinder((0, -2.14, 0.2), (0, -2.14, 0.72), 0.04, 4)
    mesh += cylinder((0, -2.14, 0.72), (0, -2.14, 0.84), 0.27, 8)
    mesh += box((-1.45, -0.42, 0.27), (0.14, 0.35, 0.06))
    for x, y, height, radius in (
        (-1.45, -0.85, 1.65, 0.35),
        (-1.45, -2.0, 2.25, 0.50),
        (1.40, -0.7, 2.25, 0.51),
        (1.55, -2.05, 2.15, 0.54),
    ):
        mesh += cylinder((x, y, 0.18), (x, y, height + 0.1), 0.024, 4)
        mesh += cylinder(
            (x, y, height), (x, y, height + 0.055), radius, 10, end_radius=0.08
        )
        for angle in (0, 2 * pi / 3, 4 * pi / 3):
            mesh += cylinder(
                (x, y, 0.28),
                (x + 0.35 * cos(angle), y + 0.35 * sin(angle), 0.14),
                0.022,
                3,
            )
    mesh += cylinder(
        (-1.45, -0.85, 1.53), (-1.45, -0.85, 1.59), 0.35, 10, end_radius=0.08
    )
    mesh += amplifiers()
    for side in (-1, 1):
        mesh += box((side * 6.5, -0.7, 1.0), (0.85, 0.7, 2.0))
        mesh += prism(
            [(-0.35, 0), (0.35, 0), (0.35, 0.15), (-0.35, 0.60)],
            1.1,
            (side * 2.7 - 0.55, 2.8, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 0, 0),
        )
        mesh += cylinder((side * 7, -3.4, 0), (side * 7, -3.4, 6.35), 0.065, 4)
    mesh += cylinder((-7, -3.4, 6.35), (7, -3.4, 6.35), 0.065, 4)
    mesh += cylinder((-7, -3.4, 5.9), (7, -3.4, 5.9), 0.065, 4)
    for x in (-6, -3, 3, 6):
        mesh += cylinder((x, -3.4, 6.3), (x + 0.3, -3.4, 5.9), 0.025, 3)
        mesh += cylinder((x, -3.0, 5.8), (x, -2.65, 5.46), 0.19, 6)
    assert len(mesh) < 4000, len(mesh)
    # Face the audience and fill GitHub's default STL camera view.
    return [
        (
            scale((-a[0], -a[1], a[2]), 3),
            scale((-b[0], -b[1], b[2]), 3),
            scale((-c[0], -c[1], c[2]), 3),
        )
        for a, b, c in mesh
    ]


def validate(mesh: list[Triangle]) -> None:
    assert mesh
    for triangle in mesh:
        unit(cross(sub(triangle[1], triangle[0]), sub(triangle[2], triangle[0])))
    edges = Counter(
        (a, b)
        for triangle in mesh
        for a, b in zip(triangle, triangle[1:] + triangle[:1], strict=True)
    )
    assert all(count == edges[(b, a)] for (a, b), count in edges.items()), (
        "Inconsistent surface winding"
    )


def write_stl(mesh: list[Triangle], path: Path) -> None:
    def number(value: float) -> str:
        return f"{value:.4g}" if abs(value) > 1e-9 else "0"

    def rounded(vertex: Vec3) -> Vec3:
        return (
            float(number(vertex[0])),
            float(number(vertex[1])),
            float(number(vertex[2])),
        )

    mesh = [(rounded(a), rounded(b), rounded(c)) for a, b, c in mesh]
    validate(mesh)
    lines = ["solid wethegods_stage"]
    for a, b, c in mesh:
        normal = unit(cross(sub(b, a), sub(c, a)))
        fields = [
            "facet normal",
            " ".join(number(value) for value in normal),
            "outer loop",
        ]
        fields.extend(
            "vertex " + " ".join(number(value) for value in vertex)
            for vertex in (a, b, c)
        )
        fields.append("endloop endfacet")
        lines.append(" ".join(fields))
    lines.append("endsolid wethegods_stage")
    content = "\n".join(lines) + "\n"
    assert len(content.encode()) < 490_000, len(content.encode())
    path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    scene = build_scene(repo / "assets/wtg-monogram.svg")
    validate(scene)
    target = repo / "assets/wethegods-stage.stl"
    write_stl(scene, target)
    print(
        f"WTG stage: {len(scene)} facets, {target.stat().st_size} bytes, winding checks passed"
    )
