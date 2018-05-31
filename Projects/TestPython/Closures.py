def multiple_of(x):
    def multiple(y):
        return x*y

    return multiple


c1 = multiple_of(5)
c2 = multiple_of(6)

print(c1(4))
print(c2(4))


def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])


def f(x):
    return 3*x


def g(x):
    return 4*x


print(f(g(2)))


