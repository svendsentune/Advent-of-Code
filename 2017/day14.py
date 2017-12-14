import day10
import itertools
import networkx as nx

def createGrid(input_key):
    used_squares = 0
    grid = []
    for r in range(128):
        row_list = []
        row_key = input_key+'-'+str(r)
        row_hash = day10.knotHash(row_key)
        binary_hash = "".join(["{0:04b}".format(int(c,16)) for c in row_hash])
        used_squares += binary_hash.count('1')
        c = 0
        for b in binary_hash:
            if b == '1':
                grid.append((r,c))
            c+=1
    return grid

def countRegions(input_key):
    grid = createGrid(input_key)
    G = nx.Graph()
    G.add_nodes_from(grid)
    for pair in list(itertools.combinations(grid,2)):
        if abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1]) == 1:
            G.add_edge(pair[0],pair[1])
    return len(list(nx.connected_components(G)))

final_test1 = "wenycdww"


print(countRegions(final_test1))
