# 最大公约数
def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


# test example
print(gcd(10, 5))
