# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 11 - "Graphs and Graph Algorithms"
# Kevin Zielinski

# Acknowledgements:
# worked with Ehab, Avraham, Kathryn, Roi


import assignment10 as gg
import networkx as nx
import matplotlib.pyplot as plt
import random


# https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
def draw_graph(matrix, file_name):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edge = (str(i), str(j))
                edges.append(edge)
    dg = nx.DiGraph()
    dg.add_edges_from(edges)
    pos = nx.spring_layout(dg)
    colors = [.5] * n
    nx.draw_networkx_nodes(dg, pos, cmap=plt.get_cmap('jet'), node_color=colors, node_size=50)
    nx.draw_networkx_labels(dg, pos)
    nx.draw_networkx_edges(dg, pos, edgelist=edges, edge_color='r', arrows=True)
    plt.savefig(file_name)
    plt.show()


# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/#
def bfs(table, s):
    result = []
    n = len(table)
    visited = [False] * n
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        v = queue.pop(0)
        result.append(v)
        for w in table[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True
    return result


def dfs_rec(table, v, visited):
    visited.append(v)
    for w in table[v]:
        if w not in visited:
            dfs_rec(table, w, visited)


def dfs(table, s):
    visited = []
    dfs_rec(table, s, visited)
    return visited


def is_cycle(matrix):
    table = gg.matrix_to_table(matrix)
    n = len(table)
    for v in range(n):
        if set(table[v]) != {(v + 1) % n, (v - 1) % n}:
            return False
    return True


def is_complete(matrix):
    table = gg.matrix_to_table(matrix)
    n = len(table)
    for v in range(n):
        if set(table[v]) != set([i for i in range(n)]) - {v}:
            return False
    return True


def is_Eulerian_Circuit(matrix):
    table = gg.matrix_to_table(matrix)
    n = len(table)
    for v in range(n):
        if set(table[v]) != set([i for i in range(n)]) - {v}:
            return False
    return True
    table = gg.matrix_to_table()


def print_graph_type(matrix):
    types = [is_cycle, is_complete, is_Eulerian_Circuit]
    for typ in types:
        print(typ.__name__, typ(matrix))


def floyd_apsp(matrix):
    n = len(matrix)
    dist = [[9999] * n for i in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j in range(n):
            dist[i][j] = matrix[i][j]
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    gg.print_matrix(dist)


def random_weighted_graph(size, is_sym, max_cost):
    matrix = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j] = random.randint(1, max_cost)
            if is_sym:
                matrix[j][i] = matrix[i][j]
            else:
                matrix[j][i] = random.randint(1, max_cost)
    return matrix


def do_graph(name, desc, matrix):
    print(desc)
    high = len(matrix) - 1
    gg.print_matrix(matrix)
    print()
    table = gg.matrix_to_table(matrix)
    gg.print_table(table)
    print()
    gg.print_graph_info(matrix)
    print()
    gg.print_graph_properties(matrix)
    print_graph_type(matrix)
    draw_graph(matrix, name + ".png")
    print("bfs starting at ", 0, bfs(table, 0))
    print("bfs starting at ", high, bfs(table, high))
    print("dfs starting at ", 0, dfs(table, 0))
    print("dfs starting at ", high, dfs(table, high))
    print()
    print()


def main():
    assn = "assignment11"
    matrix = gg.read_graph("Graph_k5.txt")
    do_graph("K5", "K5 read from file", matrix)
    # matrix_2 = gg.random_graph(10, False, .9)
    # do_graph('R10', 'Random digraph of size 10 with p = .9', matrix_2)
    matrix_3 = gg.read_graph("Graph_C4.txt")
    do_graph("C4", "C4 read from file", matrix_3)
    matrix_4 = random_weighted_graph(5, True, 99)
    gg.print_matrix(matrix_4)
    print()
    floyd_apsp(matrix_4)


if __name__ == "__main__":
    main()
