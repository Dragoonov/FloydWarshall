import sys
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

MAXINT = float("inf")
# n = 5
# m = 13
# x = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
# y = [1, 2, 3, 0, 2, 4, 3, 4, 0, 1, 4, 2, 3]
# w = [5, 4, 8, -4, -2, 5, 5, 2, -1, 2, -1, 4, 2]
df = pd.read_excel('File.xls')
n = int(df['n'][0])
m = int(df['m'][0])
x = df['x'].values
y = df['y'].values
w = df['w'].values
d = [[0 if i == j else MAXINT for i in range(n)] for j in range(n)]
p = [[-1 for k in range(n)] for p in range(n)]


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (d[i][k] == MAXINT) or (d[k][j] == MAXINT):
                    continue
                w = d[i][k] + d[k][j]
                if d[i][j] > w:
                    d[i][j] = w
                    p[i][j] = p[k][j]
    for i in range(n):
        if d[i][i] < 0:
            return False
    return True


def fw_path(i, j):
    if i == j:
        sys.stdout.write(f'{i} ')
    elif p[i][j] == -1:
        sys.stdout.write(f'NO PATH')
    else:
        fw_path(i, p[i][j])
        sys.stdout.write(f'{j} ')


for i in range(m):
    d[x[i]][y[i]] = w[i]
    p[x[i]][y[i]] = x[i]

if floyd_warshall():
    for i in range(n):
        for j in range(n):
            sys.stdout.write(f'{i}-{j}: ')
            fw_path(i, j)
            if d[i][j] < MAXINT:
                print(f'({d[i][j]})')
else:
    print(f'Negative cycle found')

G = nx.Graph()
G.add_edge('0', '1', weight=5)
G.add_edge('0', '2', weight=4)
G.add_edge('0', '3', weight=8)
G.add_edge('1', '0', weight=-4)
G.add_edge('1', '2', weight=-2)
G.add_edge('1', '4', weight=5)
G.add_edge('2', '3', weight=5)
G.add_edge('2', '4', weight=2)
G.add_edge('3', '0', weight=-1)
G.add_edge('3', '1', weight=2)
G.add_edge('3', '4', weight=-1)
G.add_edge('4', '2', weight=4)
G.add_edge('4', '3', weight=2)
nx.draw_circular(G)
plt.show()
input()
