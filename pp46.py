def roaster(zoznam):
    print('{:10}{:10}{:10}{:8}'.format('Last', 'First', 'Class', 'Average Grade'))
    for a in range(len(zoznam)):
        print('{:10}{:10}{:10}{:8.2f}'.format(zoznam[a][0], zoznam[a][1], zoznam[a][2], zoznam[a][3]))

students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympia', 'Edgar', 'Junior', 3.99])

roaster(students)
