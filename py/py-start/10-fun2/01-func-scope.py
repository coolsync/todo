# How to Modify a global variable inside a function body

a = 100

def testA():
    print(a)

def testB():
    global a
    a = 200
    print(a)

testA()
testB()

print(f'global variable a = {a}')   # a = 200
