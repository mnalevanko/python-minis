from itertools import product

def skrzat(base, number):

    def from_wb(cislo_str):
        '''wb = weird binary'''

        hodnota = 0
        for index, znak in enumerate(cislo_str[::-1]):
            cislo = int(znak)
            hodnota += (-2)**index * cislo
    
        return hodnota
    
    def to_wb(number):
        '''Converts a number in a decimal format to weird binary format.'''
    
        num_bin = bin(abs(number))
        length = len(num_bin) - 2
    
        while True:
            a = product('01', repeat=length)
            for i in a:
                pokus = ('').join(i)
                if not from_wb(pokus) == number:
                    continue
                else:
                    return(pokus)
            length += 1
            
    if base == 'b':
        cislo = from_wb(str(number))
        msg = 'From binary: {} is {}'.format(number, from_wb(str(number)))
        
    if base == 'd':
        cislo = to_wb(number)
        msg = 'To binary: {} is {}'.format(number, to_wb(number))
        
    return msg

print(skrzat('b', '01010'))
