def digit_addition(n):
    s = 0
    while n:
        s += n % 10
        if s % 2 == 0:
            s -= 2
        elif s % 2 == 1:
            s += 4
        n //= 10
    return s


print(digit_addition(432976))

