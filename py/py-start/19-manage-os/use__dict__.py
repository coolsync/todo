class A(object):
    a = 0

    def __init__(self):
        self.b = 2

aa = A()

print(aa.__dict__)      # {'b': 2}

print(A.__dict__)       

""" 
{'__module__': '__main__', 'a': 0, '__init__': <function A.__init__ at 0x7f20d9f0f0d0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
"""
