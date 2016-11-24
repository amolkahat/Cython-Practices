# This code include math.h file.
# At the run time cython compiler look in to the original decleration in math.h
# file at compile time, but cython does not parse it.

# So what exactly going on here?
# sin function is defined the way it will available to use Cython code and
# force Cython compiler to generate C code which uses the math.h file.

cdef extern from "math.h":
    cpdef double sin(double x)
