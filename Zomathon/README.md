# Zomathon: Profit-Maximizing Recommendation System (2-Day Deliverable)

This folder contains a realistic, presentation-ready mini project for a **Zomato-like food delivery platform** focused on **profit-aware recommendations**.

## What is included

1. **Problem framing + KPIs**
2. **End-to-end system architecture** (`architecture/workflow.mmd`)
3. **Database schema + ER representation** (`database/schema.sql`, `database/er_diagram.dbml`)
4. **Dummy dataset templates + sample data** (`data/*.csv`)
5. **Rule-based recommendation demo** (`demo/scoring_demo.py`)
6. **Business impact simulation** (`demo/business_impact_simulation.py`)
7. **Slide-by-slide script for a 10-12 slide PPT** (`presentation/slide_script.md`)

## Core objective

Design a recommendation system that improves:
- Conversion rate
- Average order value (AOV)
- Margin per order
- Repeat purchase rate

while respecting delivery SLA, budget constraints, and restaurant fairness.

## Quick run

```bash
python3 Zomathon/demo/scoring_demo.py
python3 Zomathon/demo/business_impact_simulation.py
```

## Recommended tools for visuals

- **PPT**: Google Slides / Canva
- **ER Diagram**: dbdiagram.io (import `database/er_diagram.dbml`)
- **Workflow Diagram**: draw.io or Mermaid-compatible renderer using `architecture/workflow.mmd`

## Delivery strategy

- **Phase 1:** Rule-based baseline with business constraints
- **Phase 2:** ML ranker (CTR/CVR + margin objective)
- **Phase 3:** Contextual personalization and budget-aware bandits
