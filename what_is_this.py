def what_is_this(param):
    
    if isinstance(param, str): return 'This is a String.'
    if param is True or param is False: return 'This is a Boolean.'
    if isinstance(param, int): return 'This is an Integer.'
    if isinstance(param, float): return 'This is a Float.'
    return 'I have no idea what this is'

print(what_is_this(True))
