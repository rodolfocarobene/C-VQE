def iteratorItemToString(item):
    name = item[0]
    name += '_' + item[1]
    name += '_' + item[2][1]
    name += '_' + item[3][1]
    if item[4] == True:
        name += '_Lag_' + item[5][0]

    return name

def fromItemIterToOption(options, item):
    option = options.copy()
    option['molecule']['basis'] = item[0]
    option['var_form_type'] = item[1]
    option['quantum_instance'] = item[2][0]
    option['optimizer'] = item[3][0]
    option['lagrange']['active'] = item[4]
    option['lagrange']['operator'] = item[5][0]
    option['lagrange']['value'] = int(item[5][1])
    option['lagrange']['multiplier'] = float(item[5][2])
    return option


