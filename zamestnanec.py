class Zamestnanec():
    '''Trieda, ktora k zadanemu menu vytvori jeho e-mailovu adresu.'''

    def __init__(self, meno, priezvisko):
        self.meno = meno.title()
        self.priezvisko = priezvisko.title()
        
    @property
    def email(self):
        return self.meno.lower() + '.' + self.priezvisko.lower() + '@gmail.com'

    def vizitka(self):
        print('{} {}'.format(self.meno.title(), self.priezvisko.title()))

emp1 = Zamestnanec('mICHAl', 'nALEVANKo')

emp1.priezvisko = 'KLIMa'

print(emp1.meno)
print(emp1.email)
emp1.vizitka()
