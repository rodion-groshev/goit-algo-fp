import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
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


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, 'ocean') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def total(root):
    if root is None:
        return 0
    return 1 + total(root.left) + total(root.right)


def color(step, total):
    main = [140, 255, 170]
    change = step / total
    new_color = [round(color * (1 - change)) for color in main]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs(root, total_steps):
    visited = set()
    lst = [root]
    colors = {}
    step = 0

    while lst:
        node = lst.pop()
        if node not in visited:
            visited.add(node)
            colors[node.id] = color(step, total_steps)
            step += 1

            if node.right:
                lst.append(node.right)
            if node.left:
                lst.append(node.left)

    return colors


def bfs(root, total=1):
    visited, queue = set(), [root]
    colors = {}
    step = 0

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            colors[node.id] = color(step, total)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

total = total(root)
dfs_colors = dfs(root, total)
draw_tree(root, dfs_colors)
bfs_colors = bfs(root, total)
draw_tree(root, bfs_colors)
