from dataclasses import dataclass


@dataclass
class BaselineWeights:
    preference_match: float = 0.35
    popularity: float = 0.20
    margin_pct: float = 0.25
    inventory_priority: float = 0.20
    prep_time_penalty: float = 0.15


def baseline_score(row: dict, w: BaselineWeights | None = None) -> float:
    if w is None:
        w = BaselineWeights()
    prep_penalty = float(row["prep_time_min"]) / 45.0
    score = (
        w.preference_match * float(row["preference_match"])
        + w.popularity * float(row["popularity"])
        + w.margin_pct * float(row["margin_pct"])
        + w.inventory_priority * float(row["inventory_priority"])
        - w.prep_time_penalty * prep_penalty
    )
    return score
