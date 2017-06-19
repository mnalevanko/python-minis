class Dataset():
    """A simple attempt to model a dataset."""

    def __init__(self, *udaje):
        self.udaje = udaje
        self.usporiadane = sorted(list(self.udaje))
        
    def median(self):
        
        if len(self.usporiadane) %2 == 0:
            index1 = int(len(self.usporiadane)/2 - 1)
            index2 = index1 + 1
            return (self.usporiadane[index1] + self.usporiadane[index2]) / 2

        else:
            index = int((len(self.usporiadane) + 1)/2 -1)
            return self.usporiadane[index]

    def priemer(self):
        return sum(list(self.udaje))/len(self.udaje)

    def q1(self):
        index1_f = (len(self.udaje) + 1) / 4

        if index1_f == int(index1_f):
            return self.usporiadane[int(index1_f) - 1]
        else:
            index1 = int((len(self.udaje) + 1) / 4) - 1
            index2 = int((len(self.udaje) + 1) / 4)
##            print(self.usporiadane[index1])
##            print(self.usporiadane[index2])
            return (self.usporiadane[index1] * 0.25 + self.usporiadane[index2] * 0.75)
            
    def q3(self):
        index1_f = ((len(self.udaje) + 1) / 4) * 3

        if index1_f == int(index1_f):
            return self.usporiadane[int(index1_f) - 1]
        else:
            index1 = int((len(self.udaje) + 1) / 4) * 3 + 1
            index2 = int((len(self.udaje) + 1) / 4) * 3 + 2
##            print(index1)
##            print(index2)
##            print(self.usporiadane[index1])
##            print(self.usporiadane[index2])
            return (self.usporiadane[index1] * 0.75 + self.usporiadane[index2] * 0.25)

    def range(self):
        return max(self.usporiadane) - min(self.usporiadane)


if __name__ == '__main__':
    o = Dataset(9,1,1,10,7,11,5,8,2)
    print(o.usporiadane)
    print('Median: {}'.format(o.median()))
    print('Priemer: {}'.format(o.priemer()))
    print('Prvy kvartil: {}'.format(o.q1()))
    print('Treti kvartil: {}'.format(o.q3()))
