# Zomathon v2: Baseline vs ML Recommendation Evaluation

This directory contains an upgraded backend-only deliverable that compares:

1. **Baseline (rule-based model)**
2. **Updated ML model (logistic regression from scratch)**

The goal is to quantify recommendation quality and business impact improvements with reproducible scripts.

## What is included

- `data/generate_synthetic_data.py` – Generates synthetic candidate recommendation data.
- `demo/baseline_model.py` – Rule-based scoring model.
- `demo/ml_model.py` – Logistic regression implementation (pure Python, no external ML libs).
- `demo/metrics.py` – Ranking/classification/business metric utilities.
- `demo/experiment_runner.py` – End-to-end baseline vs ML comparison.
- `output/` – Generated reports (CSV + JSON).

## Metrics used

### Ranking metrics
- Precision@K
- Recall@K
- NDCG@K

### Model quality metrics
- AUC
- LogLoss

### Business metrics
- Conversion@K
- AOV@K
- Profit@K

## Run sequence

```bash
python3 Zomathon_v2/data/generate_synthetic_data.py
python3 Zomathon_v2/demo/experiment_runner.py
```

## Output files

- `Zomathon_v2/output/synthetic_candidates.csv`
- `Zomathon_v2/output/model_comparison.json`
- `Zomathon_v2/output/session_predictions.csv`

## Baseline vs ML in this project

- **Baseline model** uses a transparent weighted formula:
  `score = 0.35*preference_match + 0.20*popularity + 0.25*margin_pct + 0.20*inventory_priority - 0.15*prep_time_penalty`

- **ML model** learns feature weights automatically via logistic regression to predict click probability.

This makes uplift measurable and defendable for hackathon judging.
