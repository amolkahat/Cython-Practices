pyximp = """
>>> import pyximport
>>> pyximport.install()
>>> import hello
"""
executable = """
>>> import hello
"""

try:
    import hello
    print(executable)

except:
    import pyximport
    pyximport.install()
    import hello
    print(pyximp)
