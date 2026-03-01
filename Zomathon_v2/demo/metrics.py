import math
from collections import defaultdict


def precision_recall_ndcg_at_k(rows: list[dict], score_key: str, label_key: str, k: int = 3) -> dict[str, float]:
    grouped = defaultdict(list)
    for r in rows:
        grouped[r["session_id"]].append(r)

    precisions = []
    recalls = []
    ndcgs = []

    for session_rows in grouped.values():
        sorted_rows = sorted(session_rows, key=lambda x: x[score_key], reverse=True)
        topk = sorted_rows[:k]
        rel_total = sum(int(r[label_key]) for r in session_rows)
        rel_at_k = sum(int(r[label_key]) for r in topk)

        precision = rel_at_k / k
        recall = rel_at_k / rel_total if rel_total > 0 else 0.0

        dcg = 0.0
        for i, r in enumerate(topk, start=1):
            rel = int(r[label_key])
            dcg += rel / math.log2(i + 1)

        ideal_rels = sorted([int(r[label_key]) for r in session_rows], reverse=True)[:k]
        idcg = sum(rel / math.log2(i + 1) for i, rel in enumerate(ideal_rels, start=1))
        ndcg = dcg / idcg if idcg > 0 else 0.0

        precisions.append(precision)
        recalls.append(recall)
        ndcgs.append(ndcg)

    n = len(precisions)
    return {
        f"precision@{k}": sum(precisions) / n,
        f"recall@{k}": sum(recalls) / n,
        f"ndcg@{k}": sum(ndcgs) / n,
    }


def log_loss(y_true: list[int], y_prob: list[float]) -> float:
    eps = 1e-12
    total = 0.0
    for yt, yp in zip(y_true, y_prob):
        p = min(1 - eps, max(eps, yp))
        total += yt * math.log(p) + (1 - yt) * math.log(1 - p)
    return -total / len(y_true)


def auc_score(y_true: list[int], y_prob: list[float]) -> float:
    paired = sorted(zip(y_prob, y_true), key=lambda t: t[0])
    n_pos = sum(y_true)
    n_neg = len(y_true) - n_pos
    if n_pos == 0 or n_neg == 0:
        return 0.5

    rank_sum = 0.0
    for rank, (_, label) in enumerate(paired, start=1):
        if label == 1:
            rank_sum += rank

    return (rank_sum - (n_pos * (n_pos + 1) / 2)) / (n_pos * n_neg)


def business_metrics_at_k(rows: list[dict], score_key: str, k: int = 3) -> dict[str, float]:
    grouped = defaultdict(list)
    for r in rows:
        grouped[r["session_id"]].append(r)

    conversion_hits = 0
    total_sessions = len(grouped)
    total_revenue = 0.0
    total_profit = 0.0

    for session_rows in grouped.values():
        topk = sorted(session_rows, key=lambda x: x[score_key], reverse=True)[:k]
        ordered_items = [r for r in topk if int(r["ordered"]) == 1]
        if ordered_items:
            conversion_hits += 1
        revenue = sum(float(r["price"]) for r in ordered_items)
        profit = sum(float(r["price"]) * float(r["margin_pct"]) for r in ordered_items)
        total_revenue += revenue
        total_profit += profit

    return {
        f"conversion@{k}": conversion_hits / total_sessions,
        f"aov@{k}": total_revenue / total_sessions,
        f"profit_per_session@{k}": total_profit / total_sessions,
    }
