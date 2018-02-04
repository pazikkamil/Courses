import numpy as np
from faker import Faker

fake = Faker('pl_PL')
fake.seed(4321)
print(fake.name())

np.random.standard_cauchy(1000000)
