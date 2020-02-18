def update_dictionary(d, key, value):
    if key not in d:
        x = 2 * key
        if x not in d:
            d[2 * key] = [value]
        else:
            d[2 * key] += [value]
    else:
        d[key].append(value)
