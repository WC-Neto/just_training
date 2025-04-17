import numpy as np

yuri_alberto = np.array([[24, 8, 1, 3, 1],[57, 31, 7, 8, 1]])

print(f"Gols nos últimos 2 anos: {np.sum(yuri_alberto[:, 1])}")
print(f"Assistêncais nos últimos 2 anos")