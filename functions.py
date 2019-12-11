def makeParam(data):
    param=[]
    for key, value in data.items():
        param.append(key)

    return param

def isMultiple(param, data):
    if data[param] != 1:
        return 1
    else: 
        return 0


