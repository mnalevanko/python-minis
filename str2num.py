def string2number(a_string):
    if not isinstance(a_string, str):
        raise ValueError()
    if a_string.isdigit():
        return int(a_string)
    else:
        try:
            resp = float(a_string)
            return resp
        except:
            raise ValueError()

print(string2number(False))

    
