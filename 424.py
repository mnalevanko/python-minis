def cheer(name):
    print('How do you spell winner?')
    print('I know, I know!')
    for char in name:
        print(char.upper(), end = ' ')
    print('!')
    print('And that\'s how you spell winner!')
    print('Go {}!'.format(name.title()))

cheer('huskies')
