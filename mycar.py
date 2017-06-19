class Car():

    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return 'This car is {}.'.format(self.brand)

if __name__ == '__main__':
    a = Car('Toyota')
    print(a)
