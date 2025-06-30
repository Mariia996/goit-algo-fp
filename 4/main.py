import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "lightgreen"
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання вузлів та ребер до графа."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            # Додаємо ребро між поточним вузлом та лівим дочірнім вузлом
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            # Додаємо ребро між поточним вузлом та правим дочірнім вузлом
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """Функція для візуалізації бінарного дерева."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_heap(heap):
    """Функція для візуалізації бінарної купи."""
    if not heap:
        return

    root = Node(heap[0])
    nodes = [root]
    i = 1
    while i < len(heap):
        current_node = nodes.pop(0)
        if i < len(heap):
            current_node.left = Node(heap[i])
            nodes.append(current_node.left)
            i += 1
        if i < len(heap):
            current_node.right = Node(heap[i])
            nodes.append(current_node.right)
            i += 1

    draw_tree(root)

heap = [90, 40, 60, 20, 30, 70, 51, 12]
visualize_heap(heap)
