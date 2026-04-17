def same(x, y, z):
    return x == y == z


def different(x, y, z):
    return x != y and y != z and x != z


def sorted(x, y, z):
    return x <= y <= z


print("same of 1, 2, and 3 is", same(1, 2, 3))
print("same of 3, 2, and 1 is", same(3, 2, 1))
print("same of 1, 3, and 2 is", same(1, 3, 2))
print("same of 2, 2, and 2 is", same(2, 2, 2))

print("different of 1, 2, and 3 is", different(1, 2, 3))
print("different of 3, 2, and 1 is", different(3, 2, 1))
print("different of 1, 3, and 2 is", different(1, 3, 2))
print("different of 2, 2, and 2 is", different(2, 2, 2))

print("sorted of 1, 2, and 3 is", sorted(1, 2, 3))
print("sorted of 3, 2, and 1 is", sorted(3, 2, 1))
print("sorted of 1, 3, and 2 is", sorted(1, 3, 2))
print("sorted of 2, 2, and 2 is", sorted(2, 2, 2))