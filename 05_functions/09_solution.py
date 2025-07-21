""" 
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        # print(i)
        yield i


# print(even_generator(10))

for i in even_generator(10):
    print(i) 
"""


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        # print(i)
        yield i 

# even_generator(10)
# print(even_generator(10))

for i in even_generator(10):
    print(i)