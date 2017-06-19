odpoved = 'y'
customers = []

while odpoved.lower() == 'y':
    meno, priezvisko = input('Enter customer name: ').split()
    customers.append({'fname' : meno, 'lname' : priezvisko})
    odpoved = input('Enter customer (Y/N): ')

for item in customers:
    print('{} {}'.format(item['fname'], item['lname']))
