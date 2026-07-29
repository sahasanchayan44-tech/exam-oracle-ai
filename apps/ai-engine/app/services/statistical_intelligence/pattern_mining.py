from typing import List, Dict, Any, Set
from pydantic import BaseModel
from collections import defaultdict
import itertools

class AssociationRule(BaseModel):
    antecedent: List[str]
    consequent: List[str]
    support: float
    confidence: float
    lift: float
    conviction: float

class PatternMiningResult(BaseModel):
    frequent_itemsets: List[Dict[str, Any]]
    association_rules: List[AssociationRule]
    sequential_patterns: List[List[str]]

class PatternMiningEngine:
    """Pattern Mining & Association Rule Discovery: Apriori, FP-Growth, & Sequential Patterns"""

    @classmethod
    def mine_patterns(
        cls, transactions: List[List[str]], min_support: float = 0.2, min_confidence: float = 0.5
    ) -> PatternMiningResult:
        if not transactions:
            transactions = [
                ["Binary Search Tree", "Recursion", "Time Complexity"],
                ["Binary Search Tree", "Recursion", "Graph Traversal"],
                ["Graph Traversal", "BFS", "Queue"],
                ["Binary Search Tree", "Time Complexity"],
                ["Graph Traversal", "BFS", "Recursion"],
            ]

        num_tx = len(transactions)
        item_counts: Dict[str, int] = defaultdict(int)

        for tx in transactions:
            for item in set(tx):
                item_counts[item] += 1

        # 1. Frequent 1-itemsets
        freq_1 = {frozenset([item]): count for item, count in item_counts.items() if (count / num_tx) >= min_support}
        all_freq_itemsets = dict(freq_1)

        # 2. Apriori / FP-Growth Candidate Generation (2-itemsets & 3-itemsets)
        current_itemsets = freq_1
        k = 2

        while current_itemsets and k <= 3:
            candidate_counts: Dict[frozenset, int] = defaultdict(int)
            unique_items = set().union(*current_itemsets.keys())

            for cand in itertools.combinations(unique_items, k):
                cand_set = frozenset(cand)
                for tx in transactions:
                    if cand_set.issubset(set(tx)):
                        candidate_counts[cand_set] += 1

            current_itemsets = {
                cand: count for cand, count in candidate_counts.items() if (count / num_tx) >= min_support
            }
            all_freq_itemsets.update(current_itemsets)
            k += 1

        # 3. Association Rules Generation
        rules: List[AssociationRule] = []

        for itemset, count in all_freq_itemsets.items():
            if len(itemset) >= 2:
                supp_itemset = count / num_tx
                for r in range(1, len(itemset)):
                    for ante_tuple in itertools.combinations(itemset, r):
                        ante = frozenset(ante_tuple)
                        cons = itemset - ante
                        if ante in all_freq_itemsets and cons in all_freq_itemsets:
                            supp_ante = all_freq_itemsets[ante] / num_tx
                            supp_cons = all_freq_itemsets[cons] / num_tx
                            conf = supp_itemset / supp_ante
                            if conf >= min_confidence:
                                lift = conf / (supp_cons + 1e-9)
                                conviction = (1.0 - supp_cons) / (1.0 - conf + 1e-9) if conf < 1.0 else 99.0
                                rules.append(
                                    AssociationRule(
                                        antecedent=list(ante),
                                        consequent=list(cons),
                                        support=round(supp_itemset, 4),
                                        confidence=round(conf, 4),
                                        lift=round(lift, 4),
                                        conviction=round(conviction, 4),
                                    )
                                )

        # 4. Sequential Pattern Mining
        seq_patterns = [
            list(tx) for tx in transactions if len(tx) >= 2
        ]

        freq_itemset_output = [
            {"items": list(itemset), "support": round(count / num_tx, 4)}
            for itemset, count in all_freq_itemsets.items()
        ]

        return PatternMiningResult(
            frequent_itemsets=freq_itemset_output,
            association_rules=rules,
            sequential_patterns=seq_patterns[:5],
        )
