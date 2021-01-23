# Multiplicative congruential generator
def generator(a, m, seed):
    return (a * seed) % m


X = 1  # seed > 0
a = 5**16  # multiplier
m = 2**35  # modulus

for i in range(100):
    X = generator(a, m, X)
    print(X)
