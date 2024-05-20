def test(*param):
    print(*param)
    print(param)

test(34, 4.5, 'хорош', True)

def brig(n):
    if n == 0:
        return 1
    else:
        return n * brig(n - 1)

print(brig(5))
