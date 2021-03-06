from setuptools import setup, find_packages
import os

progs = ['gmsh', 'calculix']
oses = ['win32', 'win64', 'linux32', 'linux64']
folders = []
for program in progs:
    for o in oses:
        folders.append(program+'_'+o)

# platform specific builds
# http://stackoverflow.com/questions/6469508/is-it-possible-to-express-a-platform-specific-dependency-in-setup-py-without-bui
# check -format
# check bdst -format=
# check -p for platform
# https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
# version suggestions
# http://semver.org/

setup(
    name = "pycalculix",
    install_requires = ['matplotlib >= 1.3.1', 'numpy', 'dxfgrabber'],
    version = "0.9.3",
    description = "Python 3 library to build and solve finite element analysis (FEA) models in Calculix.",
    author = "Justin Black",
    author_email = "justin.a.black@gmail.com",
    packages = find_packages(),
    include_package_data=True,
    url = "http://justinablack.com/pycalculix/",
    keywords = ["FEA", "Finite Element Analysis", "Calculix", "Mechanical Engineering", "CAD"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering"],
    long_description = """\
'''
Python 3 library to automate and build finite element analysis (FEA) models in Calculix.
----------------------------------------------------------------------------------------
Meshing uses Calculix or GMSH.
Website: http://justinablack.com/pycalculix/
Source Code: https://github.com/spacether/pycalculix
Documentation: http://spacether.github.io/pycalculix/pycalculix.html

Useful applications of Pycalculix:
-Trade studies for plane stress, plane strain, or axisymmetric parts
-Quick Kt analysis of 2D geometry
-Learning finite element analyis (FEA) and Python

Notes:
I build a chunker in python which tries to cut big areas (> 5 sides) which
cgx can't mesh into smaller areas (<= 5 sides) which are meshable in cgx.
The chunker may not always be able to cut areas correctly.

Elements Supported:
Axisymmetric, plane stress, and plane strain elements are supported.
First and second order triangles and quadrilaterals are supported.
  First order elements only have corner nodes
  Second order elements have corner and mid-side nodes
Second order elements produce more accurate results
Setting element divisions on lines is supported

Geometry Building:
One can build separate parts made of points, lines, arcs, and areas.
One can draw a part made of straight lines, then smooth out corners by adding
blends/fillets with the part method: part.fillet_lines(L1, L2, arc_radius)
The new fillet will be tangent to both adjacent lines.

Loading:
Force loading
Constant pressure
Linearly varying pressure (water pressure)
Gravity
Rotational speed forces
Displacement constraints are supported
Loads are stored on geometry primitives (points lines etc) and can be applied
before or after meshing.

Examples:
https://github.com/spacether/pycalculix/tree/master/examples
"""
)