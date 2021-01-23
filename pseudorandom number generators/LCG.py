# Linear congruential generator
def generator(a, c, m, seed):
    return (a * seed + c) % m


X = 0  # seed
a = 1664525  # multiplier
c = 1013904223  # increment
m = 2**32  # modulus

for i in range(100):
    X = generator(a, c, m, X)
    print(X)
