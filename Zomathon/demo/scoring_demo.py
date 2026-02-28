"""Simple rule-based recommendation demo.

score = user_preference_match + ctr_signal + margin_weight + delivery_time_penalty
"""

from dataclasses import dataclass


@dataclass
class Candidate:
    item_name: str
    cuisine_match: float
    ctr_signal: float
    margin_weight: float
    delivery_time_penalty: float

    @property
    def score(self) -> float:
        return (
            self.cuisine_match
            + self.ctr_signal
            + self.margin_weight
            + self.delivery_time_penalty
        )


def top_recommendations(candidates: list[Candidate], k: int = 5) -> list[Candidate]:
    return sorted(candidates, key=lambda c: c.score, reverse=True)[:k]


def main() -> None:
    user_id = 101
    candidates = [
        Candidate("Butter Chicken Meal", 0.90, 0.25, 0.40, -0.12),
        Candidate("Paneer Tikka Wrap", 0.75, 0.20, 0.35, -0.05),
        Candidate("Masala Dosa Combo", 0.30, 0.18, 0.30, -0.04),
        Candidate("Peri Peri Burger Combo", 0.55, 0.22, 0.33, -0.08),
        Candidate("Protein Power Bowl", 0.40, 0.12, 0.45, -0.03),
        Candidate("Idli Vada Combo", 0.20, 0.10, 0.28, -0.02),
    ]

    ranked = top_recommendations(candidates, k=5)

    print(f"Top 5 recommendations for user {user_id}\n")
    print(f"{'Rank':<5} {'Item':<24} {'Score':>7}")
    print("-" * 40)
    for idx, item in enumerate(ranked, start=1):
        print(f"{idx:<5} {item.item_name:<24} {item.score:>7.3f}")


if __name__ == "__main__":
    main()
