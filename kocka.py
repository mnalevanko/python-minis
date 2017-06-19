class Kocka():
    '''Abstrakcia reálnej kocky.'''

    def __init__(self, strana):
        self.strana = strana

    @staticmethod    
    def v(strana):
        return round(strana**3, 2)

    @staticmethod
    def s(strana):
        return round(strana**2, 2)

k = Kocka(3)
