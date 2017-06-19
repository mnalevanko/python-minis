def trueHandle(cup_high, cup_low, handle_high, handle_low):
    '''Tests whether the handle in a cup-with-handle base is forming in the upper half of the base.

    Takes four paramaters as input:
    * cup_high, cup_low, handle_high, handle_low
    '''
    cup_center = (cup_high + cup_low)/2
    handle_center = (handle_high + handle_low)/2

    if handle_center <= cup_center:
        return False
    else:
        return True

if __name__ == "__main__":
    ch = float(input('High of the cup: '))
    cl = float(input('Low of the cup: '))
    hh = float(input('High of the handle: '))
    hl = float(input('Low of the handle: '))

    if trueHandle:
        print('The base is OK.')
    else:
        print('The handle is too low.')
    
