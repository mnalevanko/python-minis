class ClassA(object):
    my_var = "foo"

    def do_stuff(self):
        return self.my_var


class ClassB(ClassA):
    my_var = "bar"


obj = ClassB()
print(obj.do_stuff())
