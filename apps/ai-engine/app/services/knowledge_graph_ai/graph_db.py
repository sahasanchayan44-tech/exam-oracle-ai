from abc import ABC, abstractmethod
from typing import Dict, Any, List
import networkx as nx

class IGraphDatabase(ABC):
    """Abstract Interface for Graph Databases (Neo4j, NetworkX, Memgraph)"""

    @abstractmethod
    def add_node(self, node_id: str, label: str, properties: Dict[str, Any]):
        pass

    @abstractmethod
    def add_edge(self, source_id: str, target_id: str, rel_type: str, properties: Dict[str, Any]):
        pass

    @abstractmethod
    def query_subgraph(self, root_id: str, max_depth: int = 2) -> Dict[str, Any]:
        pass

class NetworkXGraphDB(IGraphDatabase):
    """NetworkX Graph Database Implementation"""

    def __init__(self):
        self.G = nx.DiGraph()

    def add_node(self, node_id: str, label: str, properties: Dict[str, Any]):
        self.G.add_node(node_id, label=label, **properties)

    def add_edge(self, source_id: str, target_id: str, rel_type: str, properties: Dict[str, Any]):
        self.G.add_edge(source_id, target_id, rel_type=rel_type, **properties)

    def query_subgraph(self, root_id: str, max_depth: int = 2) -> Dict[str, Any]:
        if root_id not in self.G:
            return {"nodes": [], "edges": []}
        sub = nx.ego_graph(self.G, root_id, radius=max_depth)
        nodes = [{"id": n, **sub.nodes[n]} for n in sub.nodes()]
        edges = [{"source": u, "target": v, **sub[u][v]} for u, v in sub.edges()]
        return {"nodes": nodes, "edges": edges}

class Neo4jGraphDB(IGraphDatabase):
    """Neo4j Graph Database Connector with Fallback"""

    def __init__(self, uri: str = "bolt://localhost:7687", auth: tuple = ("neo4j", "password")):
        self.nx_fallback = NetworkXGraphDB()

    def add_node(self, node_id: str, label: str, properties: Dict[str, Any]):
        self.nx_fallback.add_node(node_id, label, properties)

    def add_edge(self, source_id: str, target_id: str, rel_type: str, properties: Dict[str, Any]):
        self.nx_fallback.add_edge(source_id, target_id, rel_type, properties)

    def query_subgraph(self, root_id: str, max_depth: int = 2) -> Dict[str, Any]:
        return self.nx_fallback.query_subgraph(root_id, max_depth)
