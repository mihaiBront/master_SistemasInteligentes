import argparse as arg
import logging as log

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

import Common as Comm

_log = Comm.LoggingHelper.get_logger("INFO")

def loadArgs():
    parser = arg.ArgumentParser()
    
    parser.add_argument("-n", "--number", help="ej number", type=int)
    
    args = parser.parse_args()
    
    return args.number

def ej1_nodos():
    # Matriz de adyacencia ponderada (pesos > 0 indican relevancia de las conexiones)
    A = np.array([  [0, 2, 5, 0, 0],
                    [2, 0, 3, 4, 0],
                    [5, 3, 0, 2, 0],
                    [0, 4, 2, 0, 1],
                    [0, 0, 0, 1, 0] ])

    # Crear un grafo desde la matriz de adyacencia ponderada
    G = nx.from_numpy_array(A)

    # Dibujar el grafo ponderado con etiquetas de peso en las aristas
    plt.figure(figsize=(8, 6))  # Tamaño de la figura
    pos = nx.spring_layout(G)   # Disposición de los nodos
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=16, font_color='black', edge_color='gray')

    # Añadir etiquetas a las aristas que muestran el peso
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Grafo ponderado con pesos en las aristas", size=15)
    plt.show()

    # Claude Sonet Solution (GPT failed)

    n = A.shape[0]

    objective_node = 1 #@param

    # Compute the degree matrix
    degrees = np.sum(A, axis=1)
    D = np.diag(degrees)

    # Compute the Laplacian matrix
    L = D - A

    # Remove the row and column corresponding to the objective node
    # Avoid singularity in the resolution !!!
    mask = np.ones(n, dtype=bool)
    mask[objective_node] = False
    L_reduced = L[mask][:, mask]

    # Solve the system L_reduced * x = b using np.linalg.solve
    b = np.ones(n - 1)
    x = np.linalg.solve(L_reduced, b)

    # Reconstruct the full solution vector
    full_x = np.zeros(n)
    full_x[mask] = x

    # The ranking is based on the values in full_x
    # Lower values indicate nodes more closely related to the objective node
    ranking = np.argsort(full_x)

    print(full_x)
    print(ranking)
    pass
    
def ej2_pandas():
    s1 =  pd.Series(data=[1, 2, 3, 4, 5])
    log.info(f"s1 is \n{s1}")
    s2 =  pd.Series(data=[1, 2, 3, 4, 5])
    s2 = np.invert(s1)
    log.info(f"s2 is \n{s2}")
    
    s1.plot.bar(color="black")
    plt.show(block=True)
    
    s1_np = s1.to_numpy()
    print(s1_np)
    s1_np_df = pd.DataFrame(s1_np)
    print(s1_np_df)
    
if __name__ == "__main__":
    ej = loadArgs()
    match ej:
        case 2:
            ej2_pandas()
        case _:
            ej1_nodos()
            
    
    
    