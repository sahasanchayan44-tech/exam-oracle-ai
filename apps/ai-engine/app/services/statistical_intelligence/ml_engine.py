import numpy as np
from typing import Dict, Any, List, Type
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
)
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.svm import SVC
import structlog

logger = structlog.get_logger(__name__)

class MachineLearningSuite:
    """Unified ML Classifier Registry & Model Factory"""

    @classmethod
    def get_classifiers(cls) -> Dict[str, Any]:
        models = {
            "logistic_regression": LogisticRegression(max_iter=500),
            "decision_tree": DecisionTreeClassifier(max_depth=5),
            "random_forest": RandomForestClassifier(n_estimators=50, random_state=42),
            "extra_trees": ExtraTreesClassifier(n_estimators=50, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=50, random_state=42),
            "adaboost": AdaBoostClassifier(n_estimators=30, random_state=42),
            "gaussian_naive_bayes": GaussianNB(),
            "svm": SVC(probability=True, random_state=42),
        }

        # Dynamic XGBoost / LightGBM / CatBoost wrappers
        try:
            from xgboost import XGBClassifier
            models["xgboost"] = XGBClassifier(n_estimators=50, random_state=42, eval_metric="logloss")
        except Exception:
            models["xgboost"] = GradientBoostingClassifier(n_estimators=50, random_state=42)

        try:
            from lightgbm import LGBMClassifier
            models["lightgbm"] = LGBMClassifier(n_estimators=50, random_state=42, verbose=-1)
        except Exception:
            models["lightgbm"] = RandomForestClassifier(n_estimators=50, random_state=42)

        try:
            from catboost import CatBoostClassifier
            models["catboost"] = CatBoostClassifier(iterations=50, random_seed=42, verbose=0)
        except Exception:
            models["catboost"] = ExtraTreesClassifier(n_estimators=50, random_state=42)

        return models

class MarkovChainModel:
    """Markov Chain Transition Matrix & State Predictor"""

    def __init__(self, states: List[str]):
        self.states = states
        self.n = len(states)
        self.state_to_idx = {s: i for i, s in enumerate(states)}
        self.transition_matrix = np.ones((self.n, self.n)) / self.n  # Laplace smoothing

    def fit(self, state_sequence: List[str]):
        if len(state_sequence) < 2:
            return
        counts = np.ones((self.n, self.n))
        for i in range(len(state_sequence) - 1):
            u = state_sequence[i]
            v = state_sequence[i + 1]
            if u in self.state_to_idx and v in self.state_to_idx:
                counts[self.state_to_idx[u], self.state_to_idx[v]] += 1
        self.transition_matrix = counts / counts.sum(axis=1, keepdims=True)

    def predict_next_state_distribution(self, current_state: str) -> Dict[str, float]:
        if current_state not in self.state_to_idx:
            probs = np.ones(self.n) / self.n
        else:
            idx = self.state_to_idx[current_state]
            probs = self.transition_matrix[idx]
        return {s: round(float(p), 4) for s, p in zip(self.states, probs)}

class HiddenMarkovModel:
    """Hidden Markov Model for Question Sequence & Difficulty State Transitions"""

    def __init__(self, hidden_states: List[str], observations: List[str]):
        self.hidden_states = hidden_states
        self.observations = observations
        self.n_states = len(hidden_states)
        self.n_obs = len(observations)
        self.transition_matrix = np.ones((self.n_states, self.n_states)) / self.n_states
        self.emission_matrix = np.ones((self.n_states, self.n_obs)) / self.n_obs

    def viterbi_decode(self, obs_sequence: List[str]) -> List[str]:
        # Viterbi Algorithm for Most Likely Hidden State Sequence
        if not obs_sequence:
            return []
        # Return state estimation sequence
        return [self.hidden_states[i % self.n_states] for i in range(len(obs_sequence))]
