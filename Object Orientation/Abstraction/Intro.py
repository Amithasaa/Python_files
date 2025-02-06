from abc import ABC, abstractmethod
class Demo(ABC):
    pass
    # @abstractmethod
    # def disp1(self):
    #     print('Inside display1')
    
        
d1 = Demo()

'''
1.If abstract class does not have any method then object for the abstract class can be created
'''
class Demo2(ABC):
    pass
    def disp2(self):
        print("inside disp2")
        
d2 = Demo2()
d2.disp2()
'''
2.If abstract class  have only have concrete method then object for the abstract class can be created
and concrete methods can be invoked
'''

class Demo3(ABC):
    def info(self):
        print('Inside info')
        
    @abstractmethod
    def disp3(self):
        print('Inside disp3')
        
class Demo4(Demo3):
    pass

d4 = Demo4()
d4.info()