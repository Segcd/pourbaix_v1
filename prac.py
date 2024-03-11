import matplotlib.pyplot as plt
import numpy as np

H=np.linspace(0, 1e-14, 100)

reactantes_v2 = [1,"H","e","H"]
reac_v2_bas =[]

for i in reactantes_v2:
    if i == "H":
        reactantes_v2.append(H)

print(reactantes_v2)