class testClass(): 
    x = 123

    def __init__(self):
        self.x = 5 

#Case a: get the attribute x of the class testClass()
#For case a we get 123 as the value as we are not instantiating the class
a = testClass.x
print('The attribute x of testClass is: {}'.format(str(a)))

#Case b: instantiate testClass and get the attribute x
#For case b we get 5 as the value as the act of instantiating the class utilizes the init method

b = testClass()
b = b.x
print('The attribute x of an instantiated testClass() is: {}'.format(str(b)))

#Case c: instantiate testClass, pass a value, and get the attribute x
c = testClass()
c.x = 789
print('The attribute x with a value passed is: {}'.format(str(c.x)))

