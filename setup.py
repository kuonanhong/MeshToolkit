#! /usr/bin/env python
# -*- coding:utf-8 -*- 

#
# Setup for the PyMeshToolkit package
#

# External dependencies
from setuptools import setup

# Setup configuration
setup(

    name = "PyMeshToolkit",
    version = "0.1",
    packages = ['PyMeshToolkit'],
    scripts = ['pymeshtoolkit.py'],
    author = "Michaël Roy",
    author_email = "microygh@gmail.com",
    description = "Python 3D Mesh Toolkit",
    license = "MIT",
    url = "https://github.com/microy/PyMeshToolkit"

)
