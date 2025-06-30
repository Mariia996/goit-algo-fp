import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.colors import to_hex, to_rgb

class Node:
    def __init__(self, key, color="#E1CE6F"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання вузлів та ребер до графа."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_two_trees(tree1_root, tree2_root, title1="BFS", title2="DFS"):
    """Функція для візуалізації двох дерев."""
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    for ax, root, title in zip(axs, [tree1_root, tree2_root], [title1, title2]):
        tree = nx.DiGraph()
        pos = {root.id: (0, 0)}
        tree = add_edges(tree, root, pos)
        colors = [data['color'] for _, data in tree.nodes(data=True)]
        labels = {node: data['label'] for node, data in tree.nodes(data=True)}
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
            font_color="white",
            ax=ax
        )
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()

def hex_color_gradient(start_hex, end_hex, steps):
    """Функція для створення градієнту кольорів від start_hex до end_hex."""
    start_rgb = to_rgb(start_hex)
    end_rgb = to_rgb(end_hex)
    gradient = [
        to_hex([
            start_rgb[j] + (end_rgb[j] - start_rgb[j]) * i / (steps - 1)
            for j in range(3)
        ])
        for i in range(steps)
    ]
    return gradient

def visualize_heap(heap):
    """Функція для візуалізації бінарної купи."""
    if not heap:
        return None

    root = Node(heap[0])
    nodes = [root]
    i = 1
    while i < len(heap):
        current = nodes.pop(0)
        if i < len(heap):
            current.left = Node(heap[i])
            nodes.append(current.left)
            i += 1
        if i < len(heap):
            current.right = Node(heap[i])
            nodes.append(current.right)
            i += 1
    return root

def bfs_color(tree_root, gradient):
    """Функція для обходу дерева в ширину"""
    if not tree_root:
        return

    queue = deque([tree_root])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for node, color in zip(visited, gradient):
        node.color = color

def dfs_color(tree_root, gradient):
    """Функція для обходу дерева в глибину"""
    if not tree_root:
        return

    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    for node, color in zip(visited, gradient):
        node.color = color

# Побудова дерев
heap = [99, 40, 70, 10, 50, 60, 44, 12]
tree_bfs = visualize_heap(heap)
tree_dfs = visualize_heap(heap)

total_nodes = len(heap)
gradient = hex_color_gradient("#A3412B", "#98DF74", total_nodes)

bfs_color(tree_bfs, gradient)
dfs_color(tree_dfs, gradient)

draw_two_trees(tree_bfs, tree_dfs, title1="Обхід в ширину (BFS)", title2="Обхід в глибину (DFS)")