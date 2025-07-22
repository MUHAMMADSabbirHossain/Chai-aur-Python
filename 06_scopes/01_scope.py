username = "chaiaurcode"

# def test():
#     pass

def func():
    # username = "chai"
    print(username)

print(username)

func()

x = 99

# def func2(y):
#     z = x + y
#     # print(z)
#     return z

# result = func2(1)
# print(result)

""" 
def func3():
    global x
    x = 12

func3()
print(x) 
"""

def f1():
    x = 88
    def f2():
        print(x)
    # f2()
    return f2
myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f, f(2))
print(g(3))

