import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]
    visited = set()
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous


def reconstruct_path(previous, start, end):
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
    
    path.reverse()
    
    if path[0] == start:
        return path
    else:
        return None


def visualize_graph(graph, start_vertex, distances, previous, highlight_path=None):
 
    G = nx.DiGraph()
    
    for vertex, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(vertex, neighbor, weight=weight)
    
    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    ax1.set_title('Original Graph', fontsize=14, fontweight='bold')
    
    nx.draw_networkx_edges(G, pos, ax=ax1, edge_color='gray', 
                           arrows=True, arrowsize=20, width=2,
                           connectionstyle='arc3,rad=0.1', alpha=0.6)
    
    node_colors = ['lightgreen' if node == start_vertex else 'lightblue' 
                   for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, ax=ax1, node_color=node_colors, 
                          node_size=800, edgecolors='black', linewidths=2)
    
    nx.draw_networkx_labels(G, pos, ax=ax1, font_size=12, font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax1, font_size=10)
    
    ax1.axis('off')
    ax1.set_aspect('equal')
    
    ax2.set_title(f'Shortest Path Tree from "{start_vertex}"', 
                  fontsize=14, fontweight='bold')
    
    shortest_path_edges = []
    for vertex, prev in previous.items():
        if prev is not None:
            for neighbor, weight in graph[prev]:
                if neighbor == vertex:
                    shortest_path_edges.append((prev, vertex, weight))
                    break
    
    for edge in shortest_path_edges:
        if highlight_path and edge[0] in highlight_path and edge[1] in highlight_path:
            nx.draw_networkx_edges(G, pos, [(edge[0], edge[1])], ax=ax2,
                                 edge_color='red', arrows=True, arrowsize=20,
                                 width=3, connectionstyle='arc3,rad=0.1')
        else:
            nx.draw_networkx_edges(G, pos, [(edge[0], edge[1])], ax=ax2,
                                 edge_color='green', arrows=True, arrowsize=20,
                                 width=2, connectionstyle='arc3,rad=0.1', alpha=0.7)
    
    node_colors_sp = []
    for node in G.nodes():
        if node == start_vertex:
            node_colors_sp.append('lightgreen')
        elif highlight_path and node in highlight_path:
            node_colors_sp.append('salmon')
        else:
            node_colors_sp.append('lightblue')
    
    nx.draw_networkx_nodes(G, pos, ax=ax2, node_color=node_colors_sp,
                          node_size=800, edgecolors='black', linewidths=2)
    
    labels_with_distance = {}
    for node in G.nodes():
        dist = distances[node]
        if dist == float('infinity'):
            labels_with_distance[node] = f"{node}\n(∞)"
        else:
            labels_with_distance[node] = f"{node}\n({dist})"
    
    nx.draw_networkx_labels(G, pos, labels_with_distance, ax=ax2, 
                           font_size=10, font_weight='bold')
    
    sp_edge_labels = {(e[0], e[1]): e[2] for e in shortest_path_edges}
    nx.draw_networkx_edge_labels(G, pos, sp_edge_labels, ax=ax2, font_size=10)
    
    ax2.axis('off')
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    return fig


def visualize_path(graph, start_vertex, end_vertex, distances, previous):
    """
    Visualize a specific shortest path from start to end vertex.
    """
    path = reconstruct_path(previous, start_vertex, end_vertex)
    
    if path is None:
        print(f"No path exists from {start_vertex} to {end_vertex}")
        return
    
    fig = visualize_graph(graph, start_vertex, distances, previous, highlight_path=path)
    
    path_str = ' → '.join(path)
    distance = distances[end_vertex]
    fig.suptitle(f'Highlighted Path: {path_str} (Distance: {distance})', 
                 fontsize=12, y=0.98)
    
    return fig
