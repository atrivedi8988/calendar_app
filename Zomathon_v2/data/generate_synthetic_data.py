import csv
import math
import random
from pathlib import Path

OUT_PATH = Path("Zomathon_v2/output/synthetic_candidates.csv")


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def main() -> None:
    random.seed(42)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    users = list(range(1, 151))
    items = list(range(1001, 1061))
    sessions_per_user = 8
    candidates_per_session = 10

    rows = []
    session_id = 1

    for user_id in users:
        user_pref_bias = random.uniform(0.1, 0.9)
        for _ in range(sessions_per_user):
            cart_total = random.uniform(80, 420)
            is_weekend = random.choice([0, 1])
            time_of_day = random.choice(["breakfast", "lunch", "snacks", "dinner"])

            sampled_items = random.sample(items, candidates_per_session)
            session_rows = []

            for item_id in sampled_items:
                price = random.uniform(90, 420)
                margin_pct = random.uniform(0.18, 0.55)
                prep_time_min = random.uniform(12, 45)
                popularity = random.uniform(0.15, 0.95)
                inventory_priority = random.uniform(0.0, 1.0)
                preference_match = min(1.0, max(0.0, random.gauss(user_pref_bias, 0.20)))

                prep_time_penalty = prep_time_min / 45.0

                latent = (
                    1.7 * preference_match
                    + 0.8 * popularity
                    + 0.9 * margin_pct
                    + 0.5 * inventory_priority
                    - 1.2 * prep_time_penalty
                    + (0.2 if time_of_day == "dinner" else 0.0)
                    + (0.1 if is_weekend == 1 else 0.0)
                    - 2.0
                )
                click_prob = sigmoid(latent)
                click = 1 if random.random() < click_prob else 0

                order_prob = click_prob * (0.55 + 0.30 * margin_pct)
                order = 1 if (click and random.random() < order_prob) else 0

                session_rows.append(
                    {
                        "session_id": session_id,
                        "user_id": user_id,
                        "item_id": item_id,
                        "price": round(price, 2),
                        "margin_pct": round(margin_pct, 4),
                        "prep_time_min": round(prep_time_min, 2),
                        "preference_match": round(preference_match, 4),
                        "popularity": round(popularity, 4),
                        "inventory_priority": round(inventory_priority, 4),
                        "cart_total": round(cart_total, 2),
                        "is_weekend": is_weekend,
                        "time_of_day": time_of_day,
                        "clicked": click,
                        "ordered": order,
                    }
                )

            if not any(r["clicked"] == 1 for r in session_rows):
                best = max(session_rows, key=lambda x: x["preference_match"] + x["popularity"])
                best["clicked"] = 1
            if not any(r["ordered"] == 1 for r in session_rows):
                best = max(session_rows, key=lambda x: x["margin_pct"] + x["preference_match"])
                if best["clicked"] == 1 and random.random() < 0.5:
                    best["ordered"] = 1

            rows.extend(session_rows)
            session_id += 1

    fieldnames = list(rows[0].keys())
    with OUT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
