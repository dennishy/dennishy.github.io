---
layout: post
title: "Python 3: self vs __init__"
date: 2020-06-04 12:00:00 -0000
categories: PYTHON 
---

Self represents the instance of the class, used to access the attributes and methods of the class. 

__init__ is a reserved method in classes. This constructor allows us to initialize values of the class. Furthermore, with init we can initialize multiple instances of a class that are effectively decoupled. 

Here's an example in python:


    class testClass(): 
        x = 123
        def __init__(self):
            self.x = 456
Let's look at some cases:

    #Case a: get the attribute x of the class testClass()
    #For case a we get 123 as the value as we are not instantiating the class
    a = testClass.x
    print('The attribute x of testClass is: {}'.format(str(a)))

The attribute x of testClass is 123

    #Case b: instantiate testClass and get the attribute x
    #For case b we get 456 as the value as the act of instantiating the class utilizes the init method

    b = testClass()
    print('The attribute x of an instantiated testClass() is: {}'.format(str(b.x)))

The attribute x of an instantiated testClass() is 456

    #Case c: instantiate testClass, pass a value, and get the attribute x
    c = testClass()
    c.x = 789
    print('The attribute x with a value passed is: {}'.format(str(c.x)))
  
The attribute x with a value passed is 789
