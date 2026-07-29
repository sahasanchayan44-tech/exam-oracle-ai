import pytest
from app.services.knowledge_graph.graph_service import KnowledgeGraphService

@pytest.mark.asyncio
async def test_knowledge_graph_pagerank_and_node2vec():
    graph_service = KnowledgeGraphService()
    data = [
        {"id": "q1", "concept": "Binary Search Tree", "chapter": "Trees", "tagged_concepts": ["Recursion"]},
        {"id": "q2", "concept": "AVL Tree", "chapter": "Trees", "tagged_concepts": ["Rotation"]},
    ]
    result = await graph_service.build_knowledge_graph(data)
    assert result.num_nodes > 0
    assert len(result.pagerank_scores) > 0
    assert len(result.node2vec_embeddings) > 0
    assert "nodes" in result.graph_data
