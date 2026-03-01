import csv
import json
from pathlib import Path

from baseline_model import baseline_score
from metrics import auc_score, business_metrics_at_k, log_loss, precision_recall_ndcg_at_k
from ml_model import LogisticRegressionScratch, row_to_features

DATA_PATH = Path("Zomathon_v2/output/synthetic_candidates.csv")
PRED_PATH = Path("Zomathon_v2/output/session_predictions.csv")
REPORT_PATH = Path("Zomathon_v2/output/model_comparison.json")


def load_rows() -> list[dict]:
    with DATA_PATH.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def train_test_split_by_session(rows: list[dict], train_ratio: float = 0.75) -> tuple[list[dict], list[dict]]:
    sessions = sorted({int(r["session_id"]) for r in rows})
    cut = int(len(sessions) * train_ratio)
    train_sessions = set(sessions[:cut])
    train_rows = [r for r in rows if int(r["session_id"]) in train_sessions]
    test_rows = [r for r in rows if int(r["session_id"]) not in train_sessions]
    return train_rows, test_rows


def attach_scores(train_rows: list[dict], test_rows: list[dict]) -> tuple[list[dict], list[dict]]:
    for r in train_rows:
        r["baseline_score"] = baseline_score(r)
    for r in test_rows:
        r["baseline_score"] = baseline_score(r)

    x_train = [row_to_features(r) for r in train_rows]
    y_train = [int(r["clicked"]) for r in train_rows]

    model = LogisticRegressionScratch(lr=0.12, epochs=260)
    model.fit(x_train, y_train)

    x_test = [row_to_features(r) for r in test_rows]
    ml_probs = model.predict_proba(x_test)

    for r, p in zip(test_rows, ml_probs):
        r["ml_score"] = p

    # need train ml score too for completeness if needed
    ml_train_probs = model.predict_proba(x_train)
    for r, p in zip(train_rows, ml_train_probs):
        r["ml_score"] = p

    return train_rows, test_rows


def evaluate(rows: list[dict], score_key: str, k: int = 3) -> dict:
    ranking = precision_recall_ndcg_at_k(rows, score_key=score_key, label_key="clicked", k=k)
    y_true = [int(r["clicked"]) for r in rows]
    y_prob = [float(r[score_key]) for r in rows]
    classification = {
        "auc": auc_score(y_true, y_prob),
        "logloss": log_loss(y_true, y_prob),
    }
    business = business_metrics_at_k(rows, score_key=score_key, k=k)

    combined = {}
    combined.update(ranking)
    combined.update(classification)
    combined.update(business)
    return combined


def save_predictions(rows: list[dict]) -> None:
    PRED_PATH.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "session_id",
        "user_id",
        "item_id",
        "clicked",
        "ordered",
        "price",
        "margin_pct",
        "baseline_score",
        "ml_score",
    ]
    with PRED_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r[k] for k in fields})


def main() -> None:
    rows = load_rows()
    train_rows, test_rows = train_test_split_by_session(rows)
    train_rows, test_rows = attach_scores(train_rows, test_rows)

    baseline_metrics = evaluate(test_rows, score_key="baseline_score", k=3)
    ml_metrics = evaluate(test_rows, score_key="ml_score", k=3)

    uplift = {}
    for key in ["precision@3", "recall@3", "ndcg@3", "auc", "conversion@3", "aov@3", "profit_per_session@3"]:
        b = baseline_metrics[key]
        m = ml_metrics[key]
        uplift[f"{key}_delta"] = m - b
        uplift[f"{key}_pct_change"] = ((m - b) / b * 100.0) if b != 0 else None

    report = {
        "baseline": baseline_metrics,
        "ml": ml_metrics,
        "uplift": uplift,
    }

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    save_predictions(test_rows)

    print("=== Baseline Metrics ===")
    for k, v in baseline_metrics.items():
        print(f"{k:24s}: {v:.6f}")

    print("\n=== ML Metrics ===")
    for k, v in ml_metrics.items():
        print(f"{k:24s}: {v:.6f}")

    print(f"\nSaved report to {REPORT_PATH}")
    print(f"Saved predictions to {PRED_PATH}")


if __name__ == "__main__":
    main()
