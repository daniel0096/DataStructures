from typing import Any, TypeAlias, Dict, List, Tuple
from Abstract import AbstractGraph
import DataUtils

Label: TypeAlias = str
NodeDict: TypeAlias = Dict[Label, 'LinkedGraph.GraphNode']

class LinkedGraph(AbstractGraph):
    class GraphNode(object):
        def __init__(self, label: Label):
            self.label = label
            self.edges = {}

    def __init__(self):
        self.node_dict: NodeDict = {}

    @DataUtils.requires_not_null
    def has_vertex(self, label: Label) -> bool:
        return label in self.node_dict

    @DataUtils.requires_not_null
    def add_vertex(self, vertex: Label):
        if self.has_vertex(vertex):
            print(f'Given vertex {vertex} already exists.')
            return

        new_node = self.GraphNode(vertex)
        self.node_dict[vertex] = new_node

    def edge_list(self) -> List[Tuple[Label, Label]]:
        edges = []
        for src_label, node in self.node_dict.items():
            for dst_label in node.edges:
                edges.append((src_label, dst_label))
        return edges

    def vertex_list(self) -> List[Label]:
        return list(self.node_dict.keys())

    @DataUtils.requires_not_null
    def edges(self, label: Label) -> List[Label]:
        node = self.node_dict.get(label)
        if not node:
            return []
        return list(node.edges.keys())

    def has_edge(self, src: Label, dst: Label) -> bool:
        src_node = self.node_dict.get(src)
        return dst in src_node.edges if src_node else False

    @DataUtils.requires_not_null
    def add_edge(self, src: Label, dst: Label):
        src_node = self.node_dict.get(src)
        dst_node = self.node_dict.get(dst)

        if not dst in src_node.edges:
            src_node.edges[dst] = dst_node
            return True
        return False

    def print(self):
        for label,node in self.node_dict.items():
            edges = [label for label in node.edges]
            print(f"{label}: {edges}")

# jeden z grafů
g = LinkedGraph()
# g = AdjGraph()

print(g.has_vertex('A'))
print(g.add_vertex('A'))
print(g.has_vertex('A'))
print(g.add_vertex('A'))
print(g.has_vertex('A'))
print(g.add_vertex('B'))
print()

print(g.has_edge('A','B'))
print(g.add_edge('A','B'))
print(g.has_edge('A','B'))
print(g.add_edge('A','B'))
print(g.has_edge('A','B'))
print()
print(g.add_edge('B','A'))
print(g.add_edge('B','A'))

g.add_vertex('C')
g.add_edge('C', 'B')
g.add_edge('C', 'A')

g.print()

print(g.vertex_list())
print(g.edge_list())
print(g.edges('A'))
print(g.edges('B'))
print(g.edges('C'))
print(g.edges('D'))