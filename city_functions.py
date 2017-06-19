def city_country(city, country, population=None):
    '''Return a nicely formatted text with the city and country.'''

    if population:
        return '{}, {} - population {}'.format(city.title(), country.title(), population)
    else:
        return '{}, {}'.format(city.title(), country.title())

if __name__ == '__main__':
    print(city_country('medzibrod', 'SLOVEnskO'))
    print(city_country('Vienna', 'austRIA', 1200000))
