from __future__ import annotations

import heapq
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    left: Node | None
    right: Node | None
    val: int
    color: str
    id: str

    def __init__(self, key: int, color: str = "skyblue") -> None:
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(
    graph: nx.DiGraph,
    node: Node | None,
    pos: dict[str, tuple[float, float]],
    x: float = 0,
    y: float = 0,
    layer: int = 1
) -> nx.DiGraph:
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)

            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)

            add_edges(
                graph,
                node.left,
                pos,
                x=left_x,
                y=y - 1,
                layer=layer + 1
            )

        if node.right:
            graph.add_edge(node.id, node.right.id)

            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)

            add_edges(
                graph,
                node.right,
                pos,
                x=right_x,
                y=y - 1,
                layer=layer + 1
            )

    return graph


def draw_tree(tree_root: Node) -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}

    tree = add_edges(tree, tree_root, pos)

    colors = [
        node_data["color"]
        for _, node_data in tree.nodes(data=True)
    ]

    labels = {
        node_id: node_data["label"]
        for node_id, node_data in tree.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors
    )

    plt.title("Візуалізація бінарної купи")
    plt.show()


def build_heap_tree(heap: list[int], index: int = 0) -> Node | None:
    if index >= len(heap):
        return None

    node = Node(heap[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node


if __name__ == "__main__":
    values = [10, 3, 7, 1, 14, 8, 2, 6]

    heapq.heapify(values)

    print("Масив мінімальної купи:")
    print(values)

    root = build_heap_tree(values)

    if root is not None:
        draw_tree(root)