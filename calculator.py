def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_missing(x):
    return x is None


def broken_total():
    missing_total = 0
    return missing_total
