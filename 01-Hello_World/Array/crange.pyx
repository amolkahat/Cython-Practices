def range(int a):
    cdef int i
    i = 0
    res = []
    while i < a:
        res.append(i)
        i = i + 1
    return res

