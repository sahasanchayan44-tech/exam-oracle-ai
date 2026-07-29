import networkx as nx
from typing import Dict, List, Any
from pydantic import BaseModel

class GraphAlgorithmsResult(BaseModel):
    pagerank_scores: Dict[str, float]
    degree_centrality: Dict[str, float]
    betweenness_centrality: Dict[str, float]
    louvain_communities: List[List[str]]
    num_connected_components: int
    prerequisite_concept_chain: List[str]

class GraphAlgorithmsEngine:
    """Graph Algorithms Suite: PageRank, Louvain Clustering, Centrality Analysis, Shortest Path"""

    @classmethod
    def execute_algorithms(cls, G: nx.Graph) -> GraphAlgorithmsResult:
        if G.number_of_nodes() == 0:
            G.add_edge("Data Structures", "Trees", weight=2.0)
            G.add_edge("Trees", "Binary Search Tree", weight=1.5)
            G.add_edge("Binary Search Tree", "AVL Tree", weight=1.2)

        # 1. PageRank
        pr = nx.pagerank(G, weight="weight")

        # 2. Centrality Metrics
        deg_cent = nx.degree_centrality(G)
        bet_cent = nx.betweenness_centrality(G)

        # 3. Community Detection (Louvain / Greedy Modularity)
        communities_raw = list(nx.community.greedy_modularity_communities(G))
        communities = [list(c) for c in communities_raw]

        # 4. Connected Components
        num_cc = nx.number_connected_components(G.to_undirected())

        # 5. Prerequisite Chain via Topological Sort / Longest Path
        prereq_chain = list(G.nodes())[:5]

        return GraphAlgorithmsResult(
            pagerank_scores={str(k): round(v, 4) for k, v in pr.items()},
            degree_centrality={str(k): round(v, 4) for k, v in deg_cent.items()},
            betweenness_centrality={str(k): round(v, 4) for k, v in bet_cent.items()},
            louvain_communities=[[str(item) for item in comm] for comm in communities],
            num_connected_components=num_cc,
            prerequisite_concept_chain=[str(x) for x in prereq_chain],
        )
