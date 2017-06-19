def truncatechars(a_string, num):

    if not isinstance(a_string, str) or not isinstance(num, int):
        #print('Toto je ten pripad.')
        raise(ValueError)

    dots = '...'

    if num == 0:
        return dots

    if num < len(a_string):
        return a_string[:num] + dots
    else:
        return a_string

print(truncatechars(True, 0))
