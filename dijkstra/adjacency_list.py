from typing import TypeVar, Optional, Dict, Generic, List, Tuple
import utils

T = TypeVar('T')

class AdjacencyList(Generic[T]):
    """
     Class represents an AdjacencyList
    :param Generic[T]:
    """

    def __init__(self, nodes: Optional[List[T]] = None):
        """
         initializes AdjacencyList
        :param node:
        :type Optional[T]:
        """
        self.list_nodes: List[T] = list(nodes) if nodes else []

        self.adjacency_dict: Dict[T, List[Tuple[T, int]]] = {
            node: [] for node in self.list_nodes
        }

    @utils.require_non_null
    def append_node(self, node: Optional[T]):
        """
         Appends new node in case it does not exist.

        :param node: new node object
        :type node: Optional[T]
        """
        if node not in self.list_nodes:
            self.list_nodes.append(node)
            self.adjacency_dict[node] = []

    def __repr__(self):
        return str(self.adjacency_dict)

    def __str__(self):
        return self.__repr__()

    def add_edge(self, source: T, destination: T, weight: int = 0):
        """
         Adds new edge.

        :param source: starting point A
        :type source: int
        :param destination: destination point B
        :type destination: int
        :param weight: measurable unit dependent on usage. e.g. distance.
        :type weight: int
        """
        self.append_node(source)
        self.append_node(destination)
        self.adjacency_dict[source].append((destination, weight))

    def get_edge(self, node: T) -> List[Tuple[T, int]]:
        """
         Gets an existing edge based on node input.

        :param node:
        :type node: Optional[T].
        :rtype: List[Tuple[T, int]]
        """
        return self.adjacency_dict.get(node, [])

    def draw_adjacency_list(self):
        """
         Draws an adjacency list.
        """
        for node in self.list_nodes:
            neighbors = self.adjacency_dict.get(node, [])
            formatted = ' -> '.join(f'{dest}(w={w})' for dest, w in neighbors)
            print(f'{node}: {formatted}')
