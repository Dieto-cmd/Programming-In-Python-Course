import matplotlib.pyplot as plt
import dijkstra as dij

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('E', 6), ('C', 4)],
        'B': [('C', 2), ('D', 5), ('F', 2)],
        'C': [('A', 4), ('B', 2), ('D', 3), ('E', 1)],
        'D': [('B', 5), ('C', 3), ('F', 3)],
        'E': [('C', 1), ('A', 6)],
        'F': [('B', 2), ('D', 3)]
    }
    
    start_vertex = 'F'
    
    distances, previous = dij.dijkstra(graph, start_vertex)

    dij.visualize_path(graph, start_vertex, 'E', distances, previous)
    
    plt.show()