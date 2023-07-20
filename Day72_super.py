class ParentClass:
    def parent(self):
        print("This is the parent method")
class ChildClass(ParentClass):
    def child(self):
        print("This is the child method")
        super().parent()
child_obj = ChildClass()
child_obj.child()
child_obj.parent()