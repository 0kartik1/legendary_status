#testing mro and solution of diamond problem

class top:
    def find_mro(self):
        print('Ultimate class')

class A(top):
    var_a = 'a'
    def find_mro(self):
        print('Class A')

class B(A):
    def find_mro(self):
        print('Class B')

class C(A):
    def find_mro(self):
        print('Class C')

class D(B,C):
    def find_mro(self):
        print('Class D')

class E(C,B):
    def find_mro(self):
        print('Class E')


# obj_a = A()
# A.find_mro()
# obj_b = B()
# obj_b.find_mro()
print(D.__mro__)

print(E.__mro__)
