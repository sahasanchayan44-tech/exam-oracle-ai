import json
import os
import sys
from pathlib import Path

# Add ai-engine directory to path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from app.services.knowledge_graph_ai.graph_db import NetworkXGraphDB
from app.services.knowledge_graph_ai.algorithms import GraphAlgorithmsEngine

def seed_jee_mains_dataset():
    data_path = Path(__file__).resolve().parent.parent.parent.parent.parent / "data" / "jee_mains_2015_2026" / "jee_main_2015_2026_full_dataset.json"

    if not data_path.exists():
        print(f"Dataset path not found: {data_path}")
        return

    with open(data_path, "r") as f:
        dataset = json.load(f)

    print(f"Loaded JEE Main Dataset ({dataset['year_range']}): {len(dataset['papers'])} paper shifts.")

    total_questions = 0
    graph_db = NetworkXGraphDB()

    for paper in dataset["papers"]:
        year = paper["year"]
        subject = paper["subject"]
        for q in paper["questions"]:
            total_questions += 1
            graph_db.add_node(
                node_id=q["question_id"],
                label="Question",
                properties={
                    "year": year,
                    "subject": subject,
                    "chapter": q["chapter"],
                    "concept": q["concept"],
                    "difficulty": q["difficulty"],
                },
            )
            graph_db.add_node(
                node_id=q["chapter"],
                label="Chapter",
                properties={"subject": subject},
            )
            graph_db.add_edge(
                source_id=q["question_id"],
                target_id=q["chapter"],
                rel_type="BELONGS_TO",
                properties={"weight": 1.0},
            )

    # Compute graph metrics
    results = GraphAlgorithmsEngine.execute_algorithms(graph_db.G)
    print(f"Seeded {total_questions} JEE Main questions across 2015-2026 papers into Knowledge Graph!")
    print(f"PageRank Top High-Yield Concepts: {list(results.pagerank_scores.items())[:3]}")

if __name__ == "__main__":
    seed_jee_mains_dataset()
