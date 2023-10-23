def func(x):
    return x * x

zmienna = func
print(zmienna(5))

def func2(f1, x):
    return f1(x) * x

print(func2(func, 5))

def silnia(x):
    if x <= 1:
        return  1
    else:
        return x * silnia(x - 1)

print(silnia(5))
print(silnia(7))

# !3 = 1x2x3=6  !3=6   !4=1x2x3x4x=24