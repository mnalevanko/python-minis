def hello(name):
    print('Hello, {}!'.format(name.title()))

if __name__ == '__main__':
    hello('misko')
else:
    print(__name__)
