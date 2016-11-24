def multiply_by_pi(int n):
    if n is 0:
        raise ValueError("Can not multiply with 0")
    elif isinstance(n,str):
        raise ValueError("Neumaric value required.")
    return n * 3.14159265359
