def convert_temperature(degrees, to='celsius'):
    '''Converts the degree of temperature.'''
    deg = degrees

    def to_celsius():
        result = (deg - 32) * 5 / 9
        return result

    def to_fahrenheit():
        result = deg * 9 / 5 + 32
        return result

    return to_celsius() if to == 'celsius' else to_fahrenheit()

