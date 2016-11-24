tmp1 = """
>>> import pyximport
>>> pyximport.install()
>>> import crange
>>> crange.range(10)
"""
tmp2 = """
>>> import crange
>>> crange.range(10)
"""

try:
    import crange
    print(tmp2)
    print(crange.range(10))
except:
    import pyximport
    pyximport.install()
    import crange
    print(tmp1)
    print(crange.range(10))
