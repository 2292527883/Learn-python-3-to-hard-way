import sys


class parent(object):
    def override(self):
        print("Parent override()")

    def implocot(self):
        print("Parent implicit()")

    def altered(self):
        print("Parent altered()")


class Child(parent):
    def override(self):
        print("childoverride")

    def altered(self):
        print("Child,before parent altered()")
        super().altered()
        print("Child, after oarent altered()")


dad = parent()
print("___"*30)
son = Child()
print("___"*30)
dad.implocot()
print("___"*30)
son.implocot()
print("___"*30)
dad.override()
print("___"*30)
son.override()
print("___"*30)
dad.altered()
print("___"*30)
son.altered()
help(sys)
