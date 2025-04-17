import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

yuri_alberto = np.array([[24, 8, 1, 3, 1],[57, 31, 7, 8, 1]])
df_yuri_alberto = pd.DataFrame(yuri_alberto, columns = ['Partidas', 'Gols', 'Assistências', 'Cartões Amarelos', 'Cartões Vermelhos'], index=['2025', '2024'])


print(df_yuri_alberto)
print(f"Gols nos últimos 2 anos: {np.sum(yuri_alberto[:, 1])}")
print(f"Cartões amarelos nos últimos 2 anos: {np.sum(yuri_alberto[: , 3])}")

anos = ['2025', '2024']
gols = [31, 8]

plt.bar(anos, gols, color = 'black') 
plt.title("Gols do Yuri Alberto")
plt.show()

fig = px.bar(x = anos, y = gols, title = 'gols do Yuri Alberto')
fig.show()
