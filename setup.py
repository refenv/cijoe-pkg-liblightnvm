"""
    Definition of CIJOE/liblightnvm distribution package
"""
import glob
from setuptools import setup

setup(
    name="cijoe-pkg-liblightnvm",
    version="0.0.9",
    description="CIJOE: liblightnvm package",
    author="Simon A. F. Lund",
    author_email="slund@cnexlabs.com",
    url="https://github.com/safl/cijoe-pkg-liblightnvm",
    license="BSD-2",
    install_requires=[
        "cijoe (>=0.0.16)"
    ],
    zip_safe=False,
    data_files=[
        ("share/cijoe/envs", glob.glob("envs/*")),

        ("share/cijoe/testfiles", glob.glob("testfiles/*")),
        ("share/cijoe/testcases", glob.glob("testcases/*")),
        ("share/cijoe/testsuites", glob.glob("testsuites/*")),
        ("share/cijoe/testplans", glob.glob("testplans/*"))
    ],
    options={'bdist_wheel':{'universal':True}}
)
