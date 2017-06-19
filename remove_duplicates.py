def to_fahrenheit(a_list):
    return list(map(lambda x: 9/5 * x + 32, a_list))

print(to_fahrenheit([]))
