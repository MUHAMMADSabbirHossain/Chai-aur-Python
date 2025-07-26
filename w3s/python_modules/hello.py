import mymodule
from mymodule import greeting
import mymodule as mx
import platform
from mymodule import person1


print(f"From hello.py")

mymodule.greeting("Jonathan")

greeting("Jonathan")

a = mymodule.person1["age"]

print(a)

b = mx.person1["age"]

print(b)

print(platform.system())
print(dir(mymodule))
