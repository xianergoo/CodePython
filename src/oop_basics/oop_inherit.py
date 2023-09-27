class ParentClass:
    def method(self, arg1, arg2):
        print("ParentClass method called with arguments:", arg1, arg2)

class ChildClass(ParentClass):
    def method(self, arg1, arg2, arg3):
        super().method(arg1, arg2)
        print("ChildClass method called with arguments:", arg1, arg2, arg3)

child_obj = ChildClass()
child_obj.method("arg1", "arg2", "arg3")