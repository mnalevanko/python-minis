class Stvorec():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obvod(self):
        return (self.a + self.b) * 2

    def plocha(self):
        return self.a * self.b

    def __str__(self):
        return 'Stvorec so stranami {} a {}.'.format(str(self.a), str(self.b))

if __name__ == '__main__':
    s1 = Stvorec(5, 7)
    print(s1)
