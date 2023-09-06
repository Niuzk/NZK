# Zhengkun Niu
# 9/5/2023
# 633 HW1 CODE

import scipy.integrate as spi
import numpy as np
import math
import random

# Problem(a)

def integ(x):
    return np.exp(-x**2 / 2)

result01 = spi.quad(integ, 0, 1)[0]
result04 = spi.quad(integ, 0, 4)[0]

result01 = round(result01, 3)
result04 = round(result04, 3)

print("Integral [0, 1]:" , result01)
print("Integral [0, 4]:" , result04)




print()

#Problem(b)

def integ(x):
    return np.exp(-x ** 2 / 2)

range = [(0, 1), (0, 4)]

n_value = [20, 200, 2000]

for a, b in range:
    print("Integration range:", a,",", b)

    for n in n_value:

        random_sample = np.random.uniform(a, b, n)

        integral_estimate = (b - a) * np.mean(integ(random_sample))

        print("For n =", n, "Estimate = ", integral_estimate)

