from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

ext_modules=[
        Extension("*",
                  sources=["*.pyx"],
                  libraries=["m"]),
        ]
setup(ext_modules = cythonize(ext_modules),
      include_dirs=[numpy.get_include()]
    )
