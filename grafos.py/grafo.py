import networkx as nx
import matplotlib.pyplot as plt

grafo_palavras = nx.Graph()

conexoes = [
    ("Navio", "Avião"), ("Avião", "Asa"), ("Asa", "Pássaro"),
    ("Pássaro", "Pinguim"), ("Pássaro", "Penas"), ("Asa", "Pinguim"),
    ("Penas", "Pinguim"), ("Penas", "Travesseiro"), ("Travesseiro", "Cobertor"),
    ("Cobertor", "Cama"), ("Cobertor", "Frio"), ("Frio", "Iceberg"),
    ("Iceberg", "Pinguim"), ("Iceberg", "Titanic"), ("Titanic", "Navio"),
    ("Titanic", "Oscar"), ("Oscar", "Ainda estou aqui"),
    ("Ainda estou aqui", "Ditadura militar"), ("Ditadura militar", "Getulio Vargas"),
    ("Getulio Vargas", "Petrobras"), ("Petrobras", "Petróleo"),
    ("Petróleo", "Combustível"), ("Combustível", "Avião")
]

grafo_palavras.add_edges_from(conexoes)

print("--- ANÁLISE DO GRAFO ---")
print(f"Total de Palavras (Vértices): {grafo_palavras.number_of_nodes()}")
print(f"Total de Associações (Arestas): {grafo_palavras.number_of_edges()}")

caminho = nx.shortest_path(grafo_palavras, source="Cama", target="Getulio Vargas")
print(f"\nCaminho mais curto de 'Cama' até 'Getulio Vargas':")
print(" -> ".join(caminho))

nx.draw(grafo_palavras, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=2000)
plt.show()