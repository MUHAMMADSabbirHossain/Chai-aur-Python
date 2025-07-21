def sum_all(*args):
    print(args)

    for i in args:
        print(i * 2)

    return sum(args)

print(sum_all())
print(sum_all(1))
print(sum_all(1,2))
print(sum_all(1,2,3))
# print(sum_all(1,2,3,4))
# print(sum_all(1,2,3,4,5))