# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 10 - "Binary Relations and Graphs"
# Kevin Zielinski

# Acknowledgements:
# worked with Avraham
import random
import texttable as tt


def is_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return False
    return True


def is_anti_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            return False
    return True


def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                return False
    return True


def is_anti_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                return True
            elif matrix[i][j] == 0 or matrix[j][i] == 0:
                return True
    return False


def is_transitive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 0:
                    return False
    return True


def print_graph_properties(matrix):
    properties = [is_reflexive, is_symmetric, is_transitive, is_anti_reflexive,
                  is_anti_symmetric]
    for property in properties:
        print(property.__name__, property(matrix))


def print_graph_info(matrix):
    n = len(matrix)
    in_degrees = [0] * n
    out_degrees = [0] * n
    neighbors = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                in_degrees[j] += 1
                out_degrees[i] += 1
                neighbors[i].append(j)
    print("In Degree: ", in_degrees)
    print("Out Degree: ", out_degrees)
    print("Neighbors: ", neighbors)
    data = [["Vertex", "In Degree", "Out Degree", "Neighbors"]]
    for i in range(n):
        data.append([i, in_degrees[i], out_degrees[i], neighbors[i]])
    t = tt.Texttable(max_width=200)
    t.set_cols_align(["r", "r", "r", "l"])
    t.add_rows(data)
    print(t.draw())


def random_edge(p_edge):
    return 1 if random.random() < p_edge else 0


def random_graph(size, is_sym, p_edge):
    matrix = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j] = random_edge(p_edge)
            if is_sym:
                matrix[j][i] = matrix[i][j]
            else:
                matrix[j][i] = random_edge(p_edge)
    return matrix


def print_table(table):
    print("Adjacency Table: ")
    for i in range(len(table)):
        print(i, "-->", table[i])


def matrix_to_table(am):
    table = [[] for i in range(len(am))]
    for i in range(len(am)):
        for j in range(len(am)):
            if am[i][j] == 1:
                table[i].append(j)
    return table


def print_matrix(am):
    print("Adjacency Matrix: ")
    for row in am:
        for col in row:
            print(col, end=" ")
        print()


def read_graph(file_name):
    am = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(" ")
            row = []
            for item in items:
                row.append(int(item.strip()))
            am.append(row)
        return am


def main():
    assn = "assignment10"
    matrix = read_graph("Graph_k5.txt")
    print_matrix(matrix)
    print()
    table = matrix_to_table(matrix)
    print_table(table)
    print()
    matrix_2 = random_graph(5, False, .75)
    print_matrix(matrix_2)
    print()
    matrix_3 = random_graph(5, True, .5)
    print_matrix(matrix_3)
    print()
    print_graph_info(matrix_2)
    print()
    print_graph_properties(matrix)


if __name__ == "__main__":
    main()
