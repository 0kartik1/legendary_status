from abc import ABC, abstractmethod
class test_oops:
    def __init__(self,v1,v2,v3):
        self.v1 = v1 #public classifier
        self._v2 = v2 #protected classifier
        self.__v3 = v3 #private classifier
        #self.v4 = v4
    
    @abstractmethod
    def test_vars():
        pass

oops_tester = test_oops(1,2,3)
print(oops_tester.v1)
print(oops_tester._v2) #still accessible
#print(oops_tester.__v3) #declared no such variable
# oops_tester.test_vars() #doesnt works as it is a abstract method

class test_oops_inhert(test_oops):
    def __init__(self,v1,v2,v3,v4):
        super().__init__(v1,v2,v3)
        self.v4 = v4

inhertance_test = test_oops_inhert(5,6,7,8)
print(inhertance_test.v1)
print(inhertance_test.v4)
print(inhertance_test._v2)
# print(inhertance_test.__v3) not accessible this way but can be accessed by name mangling
print(inhertance_test._test_oops__v3) # access by name mangling that is _class__privvar


    
