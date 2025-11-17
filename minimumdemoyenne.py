def minimum(valeurs):
    if len(valeurs) == 0:
        return 0
    min_val = valeurs[0]
    for v in valeurs[1:]:
        if v < min_val:
            min_val = v
    return min_val