class Stvorec():
    """Trieda, na ktorej sa ucim triedy."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plocha(self):
        """Pocita plochu stvorca."""
        return self.a * self.b

    def zvys_a(self):
        self.a += 1

a = Stvorec(3, 5)
