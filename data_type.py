def data_type(z):
    if type(z) == str:
        return len(z)
    elif z is None:
        return "no value"

    elif type(z) == bool:
        return z

    elif type(z) == int:
        if z < 100:
            return "less than 100"
    elif z == 100:
        return "Equal to 100"
    else:
        return "more than 100"

    if isinstance(z, list):
        if len(z) < 3:
            return "None"
        else:
            return z[2]




