import pandas as pd
import matplotlib.pyplot as plt


def grafico():
    graph = pd.read_json('dados_consultas.json', typ='frame', orient='columns')
    graph[['mes']].plot(kind='hist', bins=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12])
    plt.show()