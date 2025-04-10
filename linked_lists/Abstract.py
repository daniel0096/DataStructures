from typing import TypeAlias, List, Tuple
from abc import ABC, abstractmethod

Label: TypeAlias = str

class AbstractGraph(ABC):
    @abstractmethod
    def has_vertex(self, label: Label) -> bool:
        pass

    @abstractmethod
    def add_vertex(self, label: Label):
        pass

    @abstractmethod
    def add_edge(self, src: Label, dst: Label):
        pass

    @abstractmethod
    def has_edge(self, label: Label) -> bool:
        pass

    @abstractmethod
    def edges(self, label: Label) -> List[Label]:
        pass

    @abstractmethod
    def vertex_list(self) -> List[Label]:
        pass

    @abstractmethod
    def edge_list(self) -> List[Tuple[Label,Label]]:
        pass