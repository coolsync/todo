# import my_module2 as m

# m.testA()     # pass
# m.testB()     # pass

from my_module2 import *

testA()
# testB()     # NameError: name 'testB' is not defined