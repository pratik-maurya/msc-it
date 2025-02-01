import networkx as nx
import matplotlib.pyplot as plt

def create_network_graph():
  G = nx.Graph()
  G.add_node("Router A")
  G.add_node("Router B")
  G.add_node("Router C")
  G.add_node("Router D")
  G.add_node("Router E")
# Add edge representing the connections between devices
  G.add_edge("Router A", "Router B", weight =10)
  G.add_edge("Router A", "Router C", weight =15)
  G.add_edge("Router B", "Router D", weight =5)
  G.add_edge("Router C", "Router D", weight =10)
  G.add_edge("Router D", "Router E", weight =20)

  return G

def draw_network_graph(G):
  pos = nx.spring_layout(G, seed = 42)
  plt.figure(figsize=(8,6))
  nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size =3000, font_size =10, font_weight='bold')
  nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):G[u][v]['weight'] for u, v in G.edges()})
  plt.title("Network routing diagram")
  plt.axis('off')
  plt.show()

def main():
  G = create_network_graph()
  draw_network_graph(G)
  print(type(G))

if __name__ == "__main__":
  main()